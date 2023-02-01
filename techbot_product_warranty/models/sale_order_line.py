from odoo import api, fields, models
from datetime import datetime


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    warranty = fields.Boolean(string='Warranty')
    warranty_end_date = fields.Date(string='Warranty End Date')


class SaleOrderCustom(models.Model):
    _inherit = 'sale.order'

    warranty_start_date = fields.Date(string="Warranty Start Date", default=datetime.today())

    def action_confirm(self):
        for rec in self.order_line:
            if rec.warranty:
                customer = self.partner_id.id
                product_id = rec.product_id.id
                prod_id = rec.product_id.product_tmpl_id.id
                order_no = rec.order_id.id
                start_date = self.warranty_start_date
                end_date = rec.warranty_end_date
                status = 'active'
                self.env['product.warranty'].create({
                    'product_id': product_id,
                    'prod_id'  : prod_id,
                    'customer': customer,
                    'order_no': order_no,
                    'start_date': start_date,
                    'end_date': end_date,
                    'status': status
                })
        return super(SaleOrderCustom, self).action_confirm()
