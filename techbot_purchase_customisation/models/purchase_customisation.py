from odoo import fields, models


class PurchaseCustomisation(models.Model):
    _inherit = 'purchase.order'

    # prepared_signed_by_id = fields.Many2one('res.users', string="Prepared And Signed By")

