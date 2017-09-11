# -*- coding: utf-8 -*-

{
    'name': "CMO :: Purchase Level Validation",
    'summary': "",
    'author': "Phongyanon Yan.",
    'website': "http://ecosoft.co.th",
    'category': 'Purchase Management',
    "version": "1.0",
    'depends': [
        'purchase',
        'purchase_operating_unit',
    ],
    'data': [
        'views/purchase_level_validation_view.xml',
        'workflow/purchase_level_validation_workflow.xml',
        'security/ir.model.access.csv',
        'data/purchase_level_validation_data',
    ],
    'demo': [
    ],
    'installable': True,
}
