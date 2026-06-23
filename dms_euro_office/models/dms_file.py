# -*- coding: utf-8 -*-
from odoo import api, fields, models


class DmsFile(models.Model):
    _inherit = "dms.file"

    can_open_in_euro_office = fields.Boolean(
        string="Can open in Euro-Office",
        compute="_compute_can_open_euro_office",
    )

    @api.depends("extension")
    def _compute_can_open_euro_office(self):
        editable_formats = {
            "docx", "xlsx", "pptx", "docxf", "oform",
            "doc", "xls", "ppt", "odt", "ods", "odp",
            "rtf", "txt", "csv", "pdf", "djvu", "xps",
        }
        for rec in self:
            ext = (rec.extension or "").lower().lstrip(".")
            rec.can_open_in_euro_office = ext in editable_formats

    def open_in_euro_office_action(self):
        """Return an action to open this file in Euro-Office."""
        self.ensure_one()
        same_tab = self.env["ir.config_parameter"].sudo().get_param(
            "document_euro_office.same_tab", "False"
        )
        url = f"/dms_euro_office/open/{self.id}"
        return {
            "type": "ir.actions.act_url",
            "url": url,
            "target": "self" if same_tab == "True" else "new",
        }
