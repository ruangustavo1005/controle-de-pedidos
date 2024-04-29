from typing import Any, List

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPushButton

from common.gui.field.combo_box import ComboBox
from common.gui.widget.base_list_widget import BaseListWidget
from routes.cidade.repository import CidadeRepository


class ClienteListWidget(BaseListWidget):
    def __init__(
        self,
        title: str = "Cliente",
        headers: List[List[Any]] = [
            "ID",
            "Nome",
            "Telefone",
            "Cidade",
            "Qtd. de Pedidos",
        ],
        width: int = 800,
        height: int = 738,
        parent=None,
        flags=Qt.WindowFlags(),
    ):
        super().__init__(title, headers, width, height, parent, flags)
        self.table.setColumnWidth(0, 30)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(3, 200)

    def _create_actions_area(self) -> QHBoxLayout:
        layout = super()._create_actions_area()

        self.whatsapp_button = QPushButton("Chamar no WhatsApp")
        self.whatsapp_button.setFixedWidth(150)
        layout.addWidget(self.whatsapp_button)

        return layout

    def enable_row_actions(self) -> None:
        super().enable_row_actions()
        self.whatsapp_button.setDisabled(False)

    def disable_row_actions(self) -> None:
        super().disable_row_actions()
        self.whatsapp_button.setDisabled(True)

    def _create_filter_fields(self, filter_area_layout: QHBoxLayout) -> None:
        nome_label = QLabel("Nome:")
        nome_label.setFixedWidth(40)
        filter_area_layout.addWidget(nome_label)

        self.nome_filter = QLineEdit()
        self.nome_filter.setFixedWidth(100)
        filter_area_layout.addWidget(self.nome_filter)

        cidade_label = QLabel("Cidade:")
        cidade_label.setFixedWidth(55)
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
