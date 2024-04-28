from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFormLayout, QLabel, QLineEdit

from common.field.monetary_input import MonetaryInput
from common.gui.widget.base_crud_widget import BaseCRUDWidget


class ProdutoAddWidget(BaseCRUDWidget):
    def __init__(
        self,
        title: str = "Adicionar Produto",
        width: int = 300,
        height: int = 200,
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

        return layout
