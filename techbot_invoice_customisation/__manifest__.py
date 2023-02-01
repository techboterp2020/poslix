{
    'name': 'Invoice customisations',
    'version': '16.0.1.0.0',
    'author': 'Techbot',
    'category': 'Invoice',
    'license': 'LGPL-3',
    'description': """ This module manage invoice customisations...""",
    'depends': ['base', 'account', 'hr','techbot_sale_customisation'],
    'data': [
        'views/invoice_customisation_view.xml',
        'report/base_invoice_report_inherit.xml'
    ],
    'installable': True,
    'application': True,
}
