{
    'name': 'Invoice Customisation',
    'version': '16.0.1.0.0',
    'author': 'Techbot',
    'category': 'Invoice',
    'license': 'LGPL-3',
    'description': """ This module manage invoice Customisation...""",
    'depends': ['base', 'account', 'hr','techbot_sale_customisation','l10n_gcc_invoice'],
    'data': [
        'views/invoice_customisation_view.xml',
        'report/base_invoice_report_inherit.xml',
        'report/base_invoice_gcc_inherited.xml',
    ],
    'installable': True,
    'application': True,
}
