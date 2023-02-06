from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'res.partner'

    product_warranty_ids = fields.One2many('product.warranty','customer')