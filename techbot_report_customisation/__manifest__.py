{
    'name': 'Report Customisation',
    'version': '16.0.1.0.0',
    'author': 'Techbot',
    'category': 'Sale',
    'license': 'LGPL-3',
    'description': """ This module manage Report Customisation...""",
    'depends': ['base', 'sale_management', 'hr'],
    'data': [
        'report/report.xml',
        'report/delivery_slip.xml',
    ],
    'installable': True,
    'application': True,
}
