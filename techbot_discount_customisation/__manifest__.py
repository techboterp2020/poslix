# -*- coding: utf-8 -*-
{
    'name': 'Discount Customisation',
    'version': '16.0.1.1.0',
    'summary': """""",
    'category': 'Extra Tools',
    'author': 'Techbot',
    'depends': ['base','stock','sale','purchase','sale_management','account','l10n_gcc_invoice'],
    'data': [
        'views/product_template.xml',
        'report/tax_total_inherited.xml',
        'report/quotation_report.xml',
        'report/invoice_report.xml',
        'report/purchase_order_template.xml',
        'report/purchase_quotation_template.xml',
        'report/invoice_report_gcc.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,

}
