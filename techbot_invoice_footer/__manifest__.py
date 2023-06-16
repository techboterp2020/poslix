{
    'name': 'Invoice Footer',
    'version': '16.0.1.0.0',
    'author': 'Techbot',
    'category': 'Invoice',
    'license': 'LGPL-3',
    'description': """ This module manage invoice Customisation...""",
    'depends': ['base', 'account','l10n_gcc_invoice'],
    'data': [
        'report/base_invoice_gcc_inherited.xml',
    ],
    'installable': True,
    'application': True,
}
