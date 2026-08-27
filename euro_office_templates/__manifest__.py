# Copyright (C) 2026 Ascensio System SIA
# pylint: disable=pointless-statement
{
    "name": "Euro-Office Templates",
    "summary": "Automate form creation with inserting fields from Odoo in templates.",
    "description": "Work with fillable templates in Odoo using Euro-Office. Create templates based on the data and fields available in Odoo, fill them out and print with several clicks.",  # noqa: E501
    "author": "Vertel AB (port av ONLYOFFICE Templates, Ascensio System SIA)",
    "website": "https://github.com/vertelab/odoo-euro-office",
    "category": "Productivity",
    "version": "18.0.3.4.2",
    "license": "LGPL-3",
    "support": "support@vertel.se",
    "depends": ["base", "euro_office", "web"],
    "external_dependencies": {"python": ["pyjwt"]},
    "data": [
        "security/euro_office_templates_security.xml",
        "security/ir.model.access.csv",
        "views/euro_office_menu_views.xml",
        "views/res_config_settings_views.xml",
        "views/ir_actions_report_views.xml",
    ],
    "demo": ["data/templates_data.xml"],
    "images": [
        "static/description/main_screenshot.png",
        "static/description/create_templates.png",
        "static/description/edit_templates.png",
        "static/description/access_rights.png",
        "static/description/work_with_templates.png",
    ],
    "installable": True,
    "application": True,
    "assets": {
        "web.assets_backend": [
            "euro_office_templates/static/src/css/*",
            "euro_office_templates/static/src/views/**/*",
            "euro_office_templates/static/src/js/report/action_manager_report.esm.js",
        ],
    },
}
