# pylint: disable=pointless-statement
{
    "name": "Euro-Office Connector",
    "summary": "Edit and collaborate on office files within Odoo Documents.",
    "description": "Connector for Euro-Office DocumentServer (https://github.com/Euro-Office/DocumentServer). Fork of the ONLYOFFICE Odoo connector by Ascensio System SIA (LGPL-3), rebranded and maintained by Innolabs. The Euro-Office app allows users to edit and collaborate on office files within Odoo Documents using Euro-Office Docs. You can work with text documents, spreadsheets, and presentations, co-author documents in real time using two co-editing modes (Fast and Strict), Track Changes, comments, and built-in chat.",  # noqa: E501
    "author": "Innolabs.dev",
    "website": "https://github.com/innolabsdev/euro_office_odoo",
    "category": "Productivity",
    "version": "18.0.6.3.1",
    "depends": ["base", "mail"],
    "external_dependencies": {"python": ["pyjwt"]},
    # always loaded
    "data": [
        "views/templates.xml",
        "views/res_config_settings_views.xml",
    ],
    "license": "LGPL-3",
    "support": "hello@innolabs.dev",
    "images": [
        "static/description/main_screenshot.png",
        "static/description/document.png",
        "static/description/sales_section.png",
        "static/description/discuss_section.png",
        "static/description/settings.png",
    ],
    "installable": True,
    "application": True,
    "assets": {
        "web.assets_backend": [
            "euro_office_odoo/static/src/actions/*",
            "euro_office_odoo/static/src/components/*/*.xml",
            "euro_office_odoo/static/src/models/*.js",
            "euro_office_odoo/static/src/views/**/*",
            "euro_office_odoo/static/src/css/*",
        ],
    },
}
