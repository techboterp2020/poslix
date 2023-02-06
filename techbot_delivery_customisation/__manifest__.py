{
    'name': 'Delivery Customisation',
    'version': '16.0.1.0.0',
    'author': 'Techbot',

    'category': 'Product',
    'license': 'LGPL-3',
    'description': """ This module manage Delivery customisations...""",
    'depends': ['base', 'sale_management', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/delivery_custom.xml',
        'wizard/warning_wizard.xml'
    ],
    'installable': True,
    'application': True,
}