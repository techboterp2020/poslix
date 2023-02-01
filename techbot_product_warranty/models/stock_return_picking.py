from odoo import api, fields, models


class StockReturnPickings(models.TransientModel):
    _inherit = 'stock.return.picking'

    # def create_returns(self):
    #     for rec in self.product_return_moves:

            # for j in rec.product_id:
            #     if j.product_id == rec.product_id:
            #         print('haaai')
            #         status = 'expired'
            #         self.env['product.warranty'].update({
            #             'status' : status
            #         })
        # return super(StockReturnPickings, self).create_returns()
            # for rec in self.picking_id.sale_id.order_line:



