from odoo import fields, models, api


class InvoiceCustomisation(models.Model):
    _inherit = 'account.move'

    concerned_person_id = fields.Many2one('hr.employee', string="Concerned Person", related='invoice_line_ids.sale_line_ids.order_id.concerned_person_id')
    # prepared_signed_by_id = fields.Many2one('res.users', string="Prepared And Signed By")



