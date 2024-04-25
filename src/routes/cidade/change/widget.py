from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFormLayout, QLabel, QLineEdit

from common.gui.widget.base_crud_widget import BaseCRUDWidget


class CidadeChangeWidget(BaseCRUDWidget):
    def __init__(
        self,
        title: str = "Alterar Cidade",
        width: int = 300,
        height: int = 80,
        parent=None,
        flags=Qt.WindowFlags(),
    ):
        super().__init__(title, width, height, parent, flags)

    def _create_form_fields(self) -> QFormLayout:
        layout = QFormLayout()

        self.nome_field = QLineEdit()
        layout.addRow(QLabel("Nome:"), self.nome_field)

        return layout
