# -*- encoding: utf-8 -*-
{
    'name': 'USA - Ohio - Payroll',
    'author': 'Hibou Corp. <hello@hibou.io>',
    'license': 'AGPL-3',
    'category': 'Localization',
    'depends': ['l10n_us_hr_payroll'],
    'version': '0.9.0',
    'description': """
USA::Ohio Payroll Rules.
========================

    * Ohio Department of Revenue partner
    * Contribution register for Ohio DoR Unemployment
    * Contribution register for Ohio DoR Income Tax Withholding
    * Contract level Ohio Withholding Allowance
    * Company level Ohio Unemployment Rate
    """,

    'auto_install': False,
    'website': 'https://hibou.io/',
    'data':[
        'hr_payroll_view.xml',
        'data/base.xml',
        'data/rules_2016.xml',
        'data/final.xml',
    ],
    'installable': True
}
