from typing import Any, List

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPushButton

from common.gui.field.combo_box import ComboBox
from common.gui.widget.base_list_widget import BaseListWidget
from routes.cidade.repository import CidadeRepository
from routes.pedido.enum import PedidoStatusEnum


class PedidoListWidget(BaseListWidget):
    def __init__(
        self,
        title: str = "Pedido",
        headers: List[List[Any]] = [
            "ID",
            "Data e Hora",
            "Cliente",
            "Cidade",
            "Status",
            "Valor Total",
        ],
        width: int = 800,
        height: int = 738,
        parent=None,
        flags=Qt.WindowFlags(),
    ):
        super().__init__(title, headers, width, height, parent, flags)
        self.table.setColumnWidth(0, 30)
        self.table.setColumnWidth(2, 170)
        self.table.setColumnWidth(3, 120)
        self.table.setColumnWidth(5, 80)

    def _init_ui(self) -> None:
        super()._init_ui()

    def enable_row_actions(self) -> None:
        super().enable_row_actions()
        self.change_status_button.setDisabled(False)
        self.view_button.setDisabled(False)

    def disable_row_actions(self) -> None:
        super().disable_row_actions()
        self.change_status_button.setDisabled(True)
        self.view_button.setDisabled(True)

    def _create_actions_area(self) -> QHBoxLayout:
        layout = super()._create_actions_area()

        self.change_button.hide()

        self.change_status_button = QPushButton("Alterar Status")
        self.change_status_button.setFixedWidth(120)
        layout.addWidget(self.change_status_button)

        self.view_button = QPushButton("Visualizar")
        self.view_button.setFixedWidth(100)
        layout.addWidget(self.view_button)

        return layout

    def _create_filter_fields(self, filter_area_layout: QHBoxLayout) -> None:
        cliente_label = QLabel("Cliente:")
        cliente_label.setFixedWidth(45)
        filter_area_layout.addWidget(cliente_label)

        self.cliente_filter = QLineEdit()
        self.cliente_filter.setFixedWidth(100)
        filter_area_layout.addWidget(self.cliente_filter)

        cidade_label = QLabel("Cidade:")
        cidade_label.setFixedWidth(45)
        filter_area_layout.addWidget(cidade_label)

        self.cidade_filter = ComboBox()
        self.cidade_filter.setFixedWidth(150)
        self.cidade_filter.addItem("", None)
        cidade_repository = CidadeRepository()
        for cidade in cidade_repository.list_for_combo_box(
            desc_column="nome", id_column="id"
        ):
            self.cidade_filter.addItem(cidade["nome"], cidade["id"])
        filter_area_layout.addWidget(self.cidade_filter)

        status_label = QLabel("Status:")
        status_label.setFixedWidth(40)
        filter_area_layout.addWidget(status_label)

        self.status_filter = ComboBox()
        self.status_filter.setFixedWidth(100)
        self.status_filter.addItem("", None)
        for enum in PedidoStatusEnum:
            self.status_filter.addItem(enum.description, enum.value)
        self.status_filter.setCurrentIndexByData(PedidoStatusEnum.EM_PRODUCAO.value)

        filter_area_layout.addWidget(self.status_filter)
