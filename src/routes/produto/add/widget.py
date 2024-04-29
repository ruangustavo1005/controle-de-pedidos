from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFormLayout, QLabel, QLineEdit

from common.gui.field.combo_box import ComboBox
from common.gui.field.monetary_input import MonetaryInput
from common.gui.widget.base_crud_widget import BaseCRUDWidget
from routes.produto.enum import ProdutoUnidadeMedidaEnum


class ProdutoAddWidget(BaseCRUDWidget):
    def __init__(
        self,
        title: str = "Adicionar Produto",
        width: int = 300,
        height: int = 120,
        parent=None,
        flags=Qt.WindowFlags(),
    ):
        super().__init__(title, width, height, parent, flags)

    def _create_form_fields(self) -> QFormLayout:
        layout = QFormLayout()

        self.nome_field = QLineEdit()
        layout.addRow(QLabel("Nome:"), self.nome_field)

        self.preco_field = MonetaryInput()
        layout.addRow(QLabel("Preço:"), self.preco_field)

        self.unidade_medida_field = ComboBox()
        for enum in ProdutoUnidadeMedidaEnum:
            self.unidade_medida_field.addItem(enum.description, enum.value)
        layout.addRow(QLabel("Unidade de Medida:"), self.unidade_medida_field)

        return layout
