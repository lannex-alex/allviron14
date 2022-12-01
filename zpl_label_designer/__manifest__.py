# Copyright 2021 VentorTech OU
# See LICENSE file for full copyright and licensing details.

{
    'name': 'ZPL Label Designer',
    'summary': """
        Design and publish ZPL labels with easy to use interface.
    """,
    'version': '14.0.1.0.0',
    'category': 'Tools',
    "images": ["static/description/images/banner.gif"],
    'author': 'VentorTech',
    'website': 'https://ventor.tech',
    'support': 'support@ventor.tech',
    'license': 'OPL-1',
    'live_test_url': 'https://odoo.ventor.tech/',
    'price': 25.00,
    'currency': 'EUR',
    'depends': ['base', 'product', 'stock', 'product_expiry'],
    'data': [
        # Data
        'data/ir_config_parameter_data.xml',
        'data/ir_actions_server_data.xml',
        # Access rights
        'security/ir.model.access.csv',
        # Assets
        'views/assets.xml',
        # Root menus
        'views/designer_menus.xml',
        # Views
        'views/label_designer_view.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'installable': True,
    'application': True,
    "cloc_exclude": [
        "**/*"
    ]
}
