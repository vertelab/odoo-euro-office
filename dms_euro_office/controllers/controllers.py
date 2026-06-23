# -*- coding: utf-8 -*-
import logging

from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)


class DmsEuroOfficeController(http.Controller):

    @http.route("/dms_euro_office/open/<int:dms_file_id>", auth="user", type="http", website=False)
    def open_in_euro_office(self, dms_file_id, access_token=None, **kwargs):
        """Open a DMS file in Euro-Office DocumentServer.

        Finds or creates the underlying ir.attachment for the DMS file
        and redirects to the Euro-Office editor.
        """
        dms_file = request.env["dms.file"].browse(dms_file_id)
        if not dms_file.exists():
            _logger.warning("DMS file %s not found", dms_file_id)
            return request.not_found()

        # Find the ir.attachment linked to this DMS file's content_file field
        attachment = request.env["ir.attachment"].sudo().search([
            ("res_model", "=", "dms.file"),
            ("res_id", "=", dms_file_id),
            ("res_field", "=", "content_file"),
        ], limit=1)

        if not attachment:
            # Fallback: create an attachment from the DMS file content
            _logger.info("Creating attachment for DMS file %s", dms_file_id)
            attachment = request.env["ir.attachment"].sudo().create({
                "name": dms_file.name,
                "datas": dms_file.with_context(bin_size=False).content,
                "mimetype": dms_file.mimetype or "application/octet-stream",
                "res_model": "dms.file",
                "res_id": dms_file_id,
                "res_field": "content_file",
            })

        # Build the Euro-Office editor URL
        base_url = request.env["ir.config_parameter"].sudo().get_param("web.base.url")
        editor_url = f"/euro_office/editor/{attachment.id}"

        if access_token:
            editor_url += f"?access_token={access_token}"

        _logger.info("Opening DMS file %s in Euro-Office (attachment %s)", dms_file_id, attachment.id)

        # Redirect to the Euro-Office editor
        return request.redirect(editor_url, code=302)
