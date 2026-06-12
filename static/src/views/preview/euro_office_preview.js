/** @odoo-module **/

import { Component, onMounted, onWillUnmount } from "@odoo/owl"

export class EuroOfficePreview extends Component {
  static template = "euro_office_odoo.EuroOfficePreview"

  static props = {
    close: Function,
    title: String,
    url: String,
  }

  setup() {
    this.title = "Preview - " + this.props.title
    this.url =
      "/euro_office/preview" +
      `?url=${encodeURIComponent(this.props.url)}&` +
      `title=${encodeURIComponent(this.props.title)}`

    const handleKeyDown = (ev) => {
      if (ev.key === "Escape") {
        ev.stopPropagation()
        ev.preventDefault()
        this.props.close()
      }
    }

    onMounted(() => {
      document.addEventListener("keydown", handleKeyDown, { capture: true })
      document.querySelectorAll(".o-overlay-item").forEach((item) => {
        if (item.querySelector(".o-euro_office-preview")) {
          item.classList.add("o-euro_office-overlay-item")
        }
      })
    })

    onWillUnmount(() => {
      document.removeEventListener("keydown", handleKeyDown, { capture: true })
    })
  }

  onClickOutside(ev) {
    const isHeader = ev.target.closest(".o-euro_office-preview-header")
    const isBody = ev.target.closest(".o-euro_office-preview-body")

    if (!isHeader && !isBody) {
      this.props.close()
    }
  }
}
