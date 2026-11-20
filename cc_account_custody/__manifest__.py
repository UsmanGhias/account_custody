# -*- coding: utf-8 -*-
{
    'name': "Employee Cash Custody & Petty Cash Management",
    'summary': "Manage employee cash custody, petty cash advances, expense clearance, and accounting settlements",
    'description': """
Employee Cash Custody & Petty Cash Management
==============================================
Streamline employee cash custody, disbursements, petty cash advances, and settlement workflows with full double-entry accounting reconciliation:
- Custody request submission and multi-level manager approvals
- Automatic journal entry creation upon custody payment registration
- Expense line tracking against custody allowance
- Return unused amounts with automated balance settlement
- Detailed PDF Custody reports and audit trails
- Multi-company and multi-currency support
    """,
    'author': "CODCrafters, Usman Ghias",
    'website': "https://usmanghias.co.uk",
    'support': "support@codcrafters.org",
    'category': 'Accounting/Finance',
    'version': '17.0.1.0.0',
    'license': 'OPL-1',
    'price': 29.0,
    'currency': 'EUR',
    'depends': ['base', 'mail', 'account', 'hr'],
    'data': [
        'security/account_security.xml',
        'security/ir.model.access.csv',
        'data/custody_data.xml',
        'wizards/custody_line_wizard.xml',
        'views/views.xml',
        'views/report_custody.xml',
        'reports/custody_information.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
