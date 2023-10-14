# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hospital Management',
    'version': '1.0',
    'sequence': -60,
    "author": "Kenjx",
    'category': 'Hospital Management',
    'summary': 'HM Management System',
    'description': """
    HM Management System for the Advanced Users
    """,
    'depends': ['mail', 'sale','hr', 'report_xlsx'],
    'data': [
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/patient_view.xml",
        "views/female_patient_view.xml",
        "views/appointment_view.xml",
        # "reports/patient_details_template.xml",
        # "wizards/excel_report.xml",
        "reports/reports.xml",
    ],
    'demo': [
        'data/product_demo.xml',
        'data/sale_demo.xml',
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}
