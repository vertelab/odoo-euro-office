# -*- coding: utf-8 -*-
{
    'name': 'Office-redigering i Vertel',
    'version': '18.0.1.0.0',
    'summary': 'Onboardingskurs: redigera Word/Excel/PowerPoint i webbläsaren',
    'description': """
Lär dig redigera Office-dokument direkt i arbetsytan, utan att ladda ner och upp.
""",
    'author': 'Vertel Sverige AB',
    'website': 'https://vertel.se',
    'license': 'LGPL-3',
    'category': 'Website/eLearning',
    'depends': ['website_slides'],
    'data': [
        'views/slide_channel_data.xml',
    ],
    'demo': [
        'demo/slide_slide_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
