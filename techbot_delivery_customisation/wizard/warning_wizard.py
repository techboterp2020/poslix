from odoo import models


class WarningWizard(models.TransientModel):
    _name = 'warning.wizard'


    def action_ok(self):
        record = (self.env['stock.picking'].browse([self._context.get('active_id')]))
        record.check = True
        return {'type': 'ir.actions.act_window_close'}
