from odoo import api, fields, models
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    warranty = fields.Boolean(string='Warranty')
    warranty_end_date = fields.Date(string='Warranty End Date',compute='compute_warranty')

    warranty_calc = fields.Integer(string='Warranty')
    warranty_period =fields.Selection([('day', 'Day(s)'), ('month', 'Month(s)'),('year', 'Year(s)')], default='day',
        string='Warranty Period')

    @api.onchange('warranty_calc','warranty_period')
    def compute_warranty(self):
        today = fields.datetime.now().date()
        for rec in self:
            if rec.warranty_period == 'day':
                rec.warranty_end_date = today + timedelta(days=rec.warranty_calc)
            if rec.warranty_period == 'month':
                rec.warranty_end_date = today + relativedelta(months=+rec.warranty_calc)
            if rec.warranty_period == 'year':
                rec.warranty_end_date = today + relativedelta(years=rec.warranty_calc)



class SaleOrderCustom(models.Model):
    _inherit = 'sale.order'

    warranty_start_date = fields.Date(string="Warranty Start Date", default=datetime.today())

    def action_confirm(self):
        for rec in self.order_line:
            if rec.warranty:
                customer = self.partner_id.id
                product_id = rec.product_id.id
                prod_id = rec.product_id.product_tmpl_id.id
                order_no = rec.order_id.id
                start_date = self.warranty_start_date
                end_date = rec.warranty_end_date
                status = 'active'
                self.env['product.warranty'].create({
                    'product_id': product_id,
                    'prod_id'  : prod_id,
                    'customer': customer,
                    'order_no': order_no,
                    'start_date': start_date,
                    'end_date': end_date,
                    'status': status
                })
        return super(SaleOrderCustom, self).action_confirm()
