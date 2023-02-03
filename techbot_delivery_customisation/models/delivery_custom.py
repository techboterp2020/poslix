from odoo import fields, models


class StockPickingValidate(models.Model):
    _inherit = 'stock.picking'

    check = fields.Boolean(default=False)

    def button_to_validate(self):
        for rec in self.move_ids_without_package:
            picking = self.env['stock.move'].search([('product_id', '=', rec.product_id.id), ('state', '!=', 'done'), ('picking_type_id', '=', self.env.ref('stock.picking_type_out').id)])
            if len(picking) > 1 and self.picking_type_id.code == 'outgoing':
                return {
                    'name': 'Warning!!!!!!',
                    'type': 'ir.actions.act_window',
                    'view_mode': 'form',
                    'res_model': 'warning.wizard',
                    'target': 'new'
                }
            else:
                rec.picking_id.action_set_quantities_to_reservation()
                rec.picking_id.button_validate()





