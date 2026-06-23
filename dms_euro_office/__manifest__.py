{
    "name": "DMS Euro-Office Bridge",
    "summary": "Open DMS files in Euro-Office DocumentServer",
    "description": "Adds an 'Open in Euro-Office' button to DMS file views (kanban, form, list). Uses the Euro-Office DocumentServer connector for real-time collaborative editing of office documents stored in DMS.",
    "author": "Vertel AB",
    "website": "https://vertel.se",
    "category": "Productivity",
    "version": "18.0.1.0.0",
    "depends": ["dms", "document_euro_office"],
    "data": [
        "views/dms_file_views.xml",
        "security/ir.model.access.csv",
    ],
    "license": "LGPL-3",
    "installable": True,
    "application": False,
}
