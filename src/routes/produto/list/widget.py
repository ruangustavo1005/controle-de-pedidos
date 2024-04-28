from typing import Any, List

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QLabel, QLineEdit

from common.gui.widget.base_list_widget import BaseListWidget


class ProdutoListWidget(BaseListWidget):
    def __init__(
        self,
        title: str = "Produto",
        headers: List[List[Any]] = ["ID", "Nome", "Preço", "Unidade de Medida", "Qtd. de Vendas"],
        width: int = 800,
        height: int = 738,
        parent=None,
        flags=Qt.WindowFlags(),
    ):
        super().__init__(title, headers, width, height, parent, flags)
        self.table.setColumnWidth(0, 30)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 80)
        self.table.setColumnWidth(3, 120)
        self.table.setColumnWidth(4, 90)

    def _create_filter_fields(self, filter_area_layout: QHBoxLayout) -> None:
        nome_label = QLabel("Nome:")
        nome_label.setFixedWidth(40)
        filter_area_layout.addWidget(nome_label)

        self.nome_filter = QLineEdit()
        self.nome_filter.setFixedWidth(100)
        filter_area_layout.addWidget(self.nome_filter)
