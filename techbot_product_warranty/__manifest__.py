{
    'name': 'Product Warranty',
    'version': '16.0.1.0.0',
    'author': 'Techbot',

    'category': 'Product',
    'license': 'LGPL-3',
    'description': """ This module manage product Warranty...""",
    'depends': ['base', 'stock', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_warranty.xml',
        'views/sale_order_line.xml',
        'views/product_template_inherited.xml',
        'views/res_partner.xml',
        'views/warranty_data.xml',
    ],
    'installable': True,
    'application': True,
}
