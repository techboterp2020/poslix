{
    'name': 'Sale Customisation',
    'version': '16.0.1.0.0',
    'author': 'Techbot',
    'category': 'Sale',
    'license': 'LGPL-3',
    'description': """ This module manage Sale Customisation...""",
    'depends': ['base', 'sale_management', 'hr','stock','techbot_discount_customisation'],
    'data': [
        'views/sale_customisation_view.xml',
        'views/product_template.xml',
        'report/base_quotation_sale_order_report_inherit.xml',
    ],
    'installable': True,
    'application': True,
}
