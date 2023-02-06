from odoo import fields, models, api
from odoo.osv.expression import expression
from odoo.tools import float_round


class ProductProduct(models.Model):
    _inherit = 'product.template'

    salable_qty = fields.Float(string="Salable Quantity",related='product_variant_id.free_qty')
