from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools import get_lang, DEFAULT_SERVER_DATETIME_FORMAT, float_is_zero, groupby


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    @api.onchange('product_id', 'price_unit')
    def check_discount_product(self):
        for rec in self:
            if rec.product_id.discount_product:
                if rec.price_unit > 0:
                    rec.price_unit = rec.price_unit * -1


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def action_create_invoice(self):
        """ Override function for adding a discount product in the bill of a PO
        """
        precision = self.env['decimal.precision'].precision_get('Product Unit of Measure')
        # 1) Prepare invoice vals and clean-up the section lines
        invoice_vals_list = []
        sequence = 10
        for order in self:
            if order.invoice_status != 'to invoice':
                continue
            order = order.with_company(order.company_id)
            pending_section = None
            # Invoice values.
            invoice_vals = order._prepare_invoice()
            disc_line = {}
            aml_currency = self.currency_id
            date = fields.Date.today()
            for pline in order.order_line:
                if pline.product_id.discount_product:
                    disc_line.update({
                        'display_type': pline.display_type or 'product',
                        'name': '%s: %s' % (pline.order_id.name, order.name),
                        'product_id': pline.product_id.id,
                        'product_uom_id': pline.product_uom.id,
                        'quantity': pline.product_qty,
                        'price_unit': order.currency_id._convert(pline.price_unit, aml_currency, order.company_id, date,
                                                                 round=False),
                        'tax_ids': [(6, 0, pline.taxes_id.ids)],
                        'analytic_distribution': pline.analytic_distribution,
                        'purchase_line_id': pline.id,
                    })
            # Invoice line values (keep only necessary sections).
            for line in order.order_line:
                if line.display_type == 'line_section':
                    pending_section = line
                    continue
                if not float_is_zero(line.qty_to_invoice, precision_digits=precision):
                    if pending_section:
                        line_vals = pending_section._prepare_account_move_line()
                        line_vals.update({'sequence': sequence})
                        invoice_vals['invoice_line_ids'].append((0, 0, line_vals))
                        sequence += 1
                        pending_section = None
                    line_vals = line._prepare_account_move_line()
                    line_vals.update({'sequence': sequence})
                    invoice_vals['invoice_line_ids'].append((0, 0, line_vals))
                    sequence += 1
            for poline in order.order_line:
                if poline.product_id.discount_product:
                    invoice_vals['invoice_line_ids'].append((0, 0, disc_line))
            invoice_vals_list.append(invoice_vals)
            # print(invoice_vals_list,"Invooooooooooooooooooooooooooooooooooooooo")
        if not invoice_vals_list:
            raise UserError(
                _('There is no invoiceable line. If a product has a control policy based on received quantity, please make sure that a quantity has been received.'))

        # 2) group by (company_id, partner_id, currency_id) for batch creation
        new_invoice_vals_list = []
        for grouping_keys, invoices in groupby(invoice_vals_list, key=lambda x: (
        x.get('company_id'), x.get('partner_id'), x.get('currency_id'))):
            origins = set()
            payment_refs = set()
            refs = set()
            ref_invoice_vals = None
            for invoice_vals in invoices:
                if not ref_invoice_vals:
                    ref_invoice_vals = invoice_vals
                else:
                    ref_invoice_vals['invoice_line_ids'] += invoice_vals['invoice_line_ids']
                origins.add(invoice_vals['invoice_origin'])
                payment_refs.add(invoice_vals['payment_reference'])
                refs.add(invoice_vals['ref'])
            ref_invoice_vals.update({
                'ref': ', '.join(refs)[:2000],
                'invoice_origin': ', '.join(origins),
                'payment_reference': len(payment_refs) == 1 and payment_refs.pop() or False,
            })
            new_invoice_vals_list.append(ref_invoice_vals)
        invoice_vals_list = new_invoice_vals_list
        # 3) Create invoices.
        moves = self.env['account.move']
        AccountMove = self.env['account.move'].with_context(default_move_type='in_invoice')
        for vals in invoice_vals_list:
            moves |= AccountMove.with_company(vals['company_id']).create(vals)
        # 4) Some moves might actually be refunds: convert them if the total amount is negative
        # We do this after the moves have been created since we need taxes, etc. to know if the total
        # is actually negative or not
        moves.filtered(
            lambda m: m.currency_id.round(m.amount_total) < 0).action_switch_invoice_into_refund_credit_note()
        return self.action_view_invoice(moves)
