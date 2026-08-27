/** @odoo-module */
// Copyright (C) 2026 Ascensio System SIA

import { registry } from "@web/core/registry"
import { kanbanView } from "@web/views/kanban/kanban_view"
import { OnlyofficeKanbanController } from "./euro_office_kanban_controller"
import { OnlyofficeKanbanRenderer } from "./euro_office_kanban_renderer"

export const euro_officeKanbanView = {
  ...kanbanView,
  Controller: OnlyofficeKanbanController,
  Renderer: OnlyofficeKanbanRenderer,
  buttonTemplate: "euro_office_templates.KanbanView.Buttons",
}

registry.category("views").add("euro_office_kanban", euro_officeKanbanView)
