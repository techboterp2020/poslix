from odoo import fields, models, api, _
from odoo.exceptions import UserError


class SaleCustomisation(models.Model):
    _inherit = 'sale.order'

    concerned_person_id = fields.Many2one('hr.employee', string="Concerned Person")

    # prepared_signed_by_id = fields.Many2one('res.users', string="Signed By")

    def action_confirm(self):
        lst = []
        for rec in self.order_line:
            if rec.product_id.detailed_type == 'product':
                if rec.product_uom_qty > rec.product_id.free_qty:
                    lst.append(rec.product_id.name)
        not_avb_prdct = ', '.join(lst)
        if not_avb_prdct:
            raise UserError(_("'%s' Product Quantity Not Available For Sale.", not_avb_prdct))
        return super(SaleCustomisation, self).action_confirm()





class SaleOrderLines(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_id', 'product_uom_qty')
    def check_product_qty(self):
        if self.order_id.state == 'sale':
            if self.product_id.detailed_type == 'product':
                if self.product_uom_qty > self.product_id.free_qty:
                    raise UserError(_("Product Quantity Not Available For Sale.", ))

    # @api.onchange('product_id')
    # def check_prod_qty(self):
    #     if self.order_id.state == 'sale':
    #             if self.product_uom_qty == 1:
    #                 return {
    #                     'warning': {
    #                         'title': "Something bad happened",
    #                         'message': "It was very bad indeed",
    #                     }
    #                 }
