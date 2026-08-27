/** @odoo-module **/
// Copyright (C) 2026 Ascensio System SIA

import { KanbanRenderer } from "@web/views/kanban/kanban_renderer"
import { EuroOfficeKanbanRecord } from "./euro_office_kanban_record"

export class EuroOfficeKanbanRenderer extends KanbanRenderer {
  setup() {
    super.setup(...arguments)
  }

  /**
   * @override
   **/
  canQuickCreate() {
    return false
  }

  /**
   * @override
   **/
  canCreateGroup() {
    return false
  }
}

EuroOfficeKanbanRenderer.components = {
  ...KanbanRenderer.components,
  KanbanRecord: EuroOfficeKanbanRecord,
}
