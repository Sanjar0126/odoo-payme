# -*- coding: utf-8 -*-
{
    'name': "Payme",

    'summary': """
        Payme""",

    'description': """
        Long description for payme
    """,

    'author': "Sanjar",
    'website': "https://t.me/Sanjar8994",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Payment',
    'version': '0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'payment'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
