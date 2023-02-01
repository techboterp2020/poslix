from odoo import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    @api.onchange('product_id', 'price_unit')
    def check_discount_product(self):
        for rec in self:
            if rec.product_id.discount_product:
                if rec.price_unit > 0:
                    rec.price_unit = rec.price_unit * -1
