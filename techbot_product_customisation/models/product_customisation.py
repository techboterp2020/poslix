from odoo import fields, models


class ProductTemplateCustomisation(models.Model):
    _inherit = 'product.template'

    company_id = fields.Many2one(
        'res.company', 'Company',
        default=lambda self: self.env.company)

