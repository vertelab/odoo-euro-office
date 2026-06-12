# Euro-Office Connector for Odoo

Edit and collaborate on office files (docx, xlsx, pptx, PDF forms) inside Odoo
using a self-hosted [Euro-Office DocumentServer](https://github.com/Euro-Office/DocumentServer).

This module is a fork of the [ONLYOFFICE Odoo connector](https://github.com/ONLYOFFICE/onlyoffice_odoo)
by Ascensio System SIA (LGPL-3), rebranded and maintained by
[Innolabs](https://innolabs.dev) for the Euro-Office DocumentServer, which is
API-compatible with ONLYOFFICE Docs.

## Changes vs upstream

- Renamed module, routes (`/euro_office/...`), model and config parameters
- **Fixed swapped settings fields**: upstream put `doc_server_odoo_url` under
  the "Docs address for internal requests" label and vice-versa, causing
  users to point the Document Server at itself (404 on file download)
- Settings page trimmed to functional options; ONLYOFFICE demo-server and
  marketing blocks removed
- Routes use Odoo 19 `type="jsonrpc"` (upstream 6.3.0 still shipped
  `type="json"`, which Odoo 19 removed)
- Translations (i18n) dropped pending re-extraction of rebranded strings

## Requirements

- Odoo 19
- A running Euro-Office DocumentServer reachable over HTTPS
- Python `pyjwt` (add to your `requirements.txt` on Odoo.sh)

## Configuration

Settings → Euro-Office:

| Setting | Value |
|---------|-------|
| Document Server address | Public URL of your Euro-Office server |
| Secret key (JWT) | Same secret as configured on the Document Server |
| Advanced → Document Server address for requests from Odoo | Only if Odoo must use a different (internal) URL |
| Advanced → Odoo address for requests from the Document Server | Only if the server cannot use Odoo's base URL |

Saving runs a connectivity test (the Document Server downloads a test file
from Odoo and converts it) — both directions must be reachable.

## License

LGPL-3.0 — see [LICENSE](LICENSE). Original work
(c) Ascensio System SIA 2024; modifications (c) Innolabs 2026.
