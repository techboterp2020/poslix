from odoo import api,models,fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    discount_product = fields.Boolean(string="Discount Product")
