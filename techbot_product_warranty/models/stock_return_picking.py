from odoo import api, fields, models


class StockReturnPickings(models.TransientModel):
    _inherit = 'stock.return.picking'

    def create_returns(self):
        order_no = self.picking_id.sale_id.name
        print(order_no)
        for rec in self.product_return_moves:
            products = rec.product_id.id
            qty = int(rec.quantity)
            warrantys = self.env['product.warranty'].search([('order_no', '=', order_no),('product_id','=',products),('status','=','active')],limit = qty)
            if warrantys:
                print(qty)
                for war in warrantys:
                    status = 'cancelled'
                    for i in range(qty):
                        war.write({
                            'status' : status
                        })
                    print(war.status)
                    # print(self.kkkkk)
        return super(StockReturnPickings, self).create_returns()



