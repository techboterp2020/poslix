from odoo import api, fields, models
from datetime import datetime

class ProductWarranty(models.Model):
    _name = 'product.warranty'
    _rec_name = 'product_id'


    product_id = fields.Many2one('product.product', string='Product',required=True)
    prod_id = fields.Many2one('product.template',string='Product')
    customer = fields.Many2one('res.partner',string='Customer')
    order_no = fields.Many2one('sale.order',string="Order")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    status = fields.Selection(
        selection=[
            ('active', "Active"),
            ('expired', "Expired"),
            ('cancelled','Cancelled')
        ],
        string="Status",
        store=True)

    def update_status(self):
        self.env['product.warranty'].search([('end_date','<',fields.Date.today())]).write({'status':'expired'})

