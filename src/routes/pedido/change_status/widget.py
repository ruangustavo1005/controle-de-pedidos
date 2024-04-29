from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFormLayout, QLabel, QLayout

from common.gui.field.combo_box import ComboBox
from common.gui.widget.base_crud_widget import BaseCRUDWidget
from routes.pedido.enum import PedidoStatusEnum


class PedidoStatusChangeWidget(BaseCRUDWidget):
    def __init__(
        self,
        title: str = "Alterar Status do Pedido",
        width: int = 300,
        height: int = 80,
        parent=None,
        flags=Qt.WindowFlags(),
    ):
        super().__init__(title, width, height, parent, flags)

    def _create_form_fields(self) -> QLayout:
        layout = QFormLayout()

        self.status_field = ComboBox()
        for enum in PedidoStatusEnum:
            self.status_field.addItem(enum.description, enum.value)
        layout.addRow(QLabel("Novo status:"), self.status_field)

        return layout
