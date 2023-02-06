{
    'name': 'Purchase Customisation',
    'version': '16.0.1.0.0',
    'author': 'Techbot',
    'category': 'Purchase',
    'license': 'LGPL-3',
    'description': """ This module manage purchase customisations...""",
    'depends': ['base', 'purchase'],
    'data': [
        'report/base_purchase_order_report_inherit.xml',
        'report/base_purchase_quotation_report_inherit.xml',
    ],
    'installable': True,
    'application': True,
}
