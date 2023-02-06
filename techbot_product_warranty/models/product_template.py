from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    product_warranty_ids = fields.One2many('product.warranty', 'product_id')


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_warranty_ids = fields.One2many('product.warranty', 'prod_id')
