from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFormLayout, QLabel, QLineEdit

from common.gui.field.combo_box import ComboBox
from common.gui.widget.base_crud_widget import BaseCRUDWidget
from routes.cidade.repository import CidadeRepository


class ClienteAddWidget(BaseCRUDWidget):
    def __init__(
        self,
        title: str = "Adicionar Cliente",
        width: int = 300,
        height: int = 130,
        parent=None,
        flags=Qt.WindowFlags(),
    ):
        super().__init__(title, width, height, parent, flags)

    def _create_form_fields(self) -> QFormLayout:
        layout = QFormLayout()

        self.nome_field = QLineEdit()
        layout.addRow(QLabel("Nome:"), self.nome_field)

        self.telefone_field = QLineEdit()
        layout.addRow(QLabel("Telefone:"), self.telefone_field)

        self.cidade_field = ComboBox()
        cidade_repository = CidadeRepository()
        for cidade in cidade_repository.list_for_combo_box(
            desc_column="nome", id_column="id"
        ):
            self.cidade_field.addItem(cidade["nome"], cidade["id"])
        layout.addRow(QLabel("Cidade:"), self.cidade_field)

        return layout
