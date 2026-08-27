Prerequisites
=============

To be able to work with office files within Odoo Enterprise, you will need an instance of `Euro-Office Docs <https://www.euro_office.com/download-docs.aspx>`_.

**Please note:** You need to obtain a license for Euro-Office Docs with the included Automation API option.

**Please note**: Euro-Office demo templates will only be added to the Odoo modules that are already installed. That's why we strongly recommend installing Euro-Office Templates after installing other Odoo modules such as CRM, Sales, Calendar, etc.

Euro-Office app configuration
============================

All the settings are configured from the `main Euro-Office app for Odoo <https://apps.odoo.com/apps/modules/18.0/euro_office>`_.

To adjust the main app settings within your Odoo, go to *Home menu -> Settings -> Euro-Office*.

In the **Document Server Url**, specify the URL of the installed Euro-Office Docs or the address of Euro-Office Docs Cloud.

**Document Server JWT Secret**: JWT is enabled by default and the secret key is generated automatically to restrict the access to Euro-Office Docs. if you want to specify your own secret key in this field, also specify the same secret key in the Euro-Office Docs `config file <https://api.euro_office.com/docs/docs-api/additional-api/signature/>`_ to enable the validation.

**Document Server JWT Header**: Standard JWT header used in Euro-Office is Authorization. In case this header is in conflict with your setup, you can change the header to the custom one.

In case your network configuration doesn't allow requests between the servers via public addresses, specify the Euro-Office Docs address for internal requests from the Odoo server and vice versa.

If you would like the editors to open in the same tab instead of a new one, check the corresponding setting "Open file in the same tab".

.. image:: settings.png
    :width: 800


Contact us
============================
If you have any questions or suggestions regarding the Euro-Office app for Odoo, please let us know at `forum.euro_office.com <https://forum.euro_office.com>`_.
