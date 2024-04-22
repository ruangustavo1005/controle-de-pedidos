from PySide6.QtWidgets import (
    QTableView,
    QVBoxLayout,
    QWidget,
    QAbstractItemView,
    QPushButton,
)
from PySide6.QtCore import Qt

from common.gui.core.table_model_default import TableModelDefault


class BaseListWidget(QWidget):
    def __init__(
        self,
        title: str,
        width: int = 800,
        height: int = 800,
        parent=None,
        flags=Qt.WindowFlags()
    ):
        super(BaseListWidget, self).__init__(parent, flags)
        self.setWindowTitle(title)
        self.resize(width, height)
        self.initUI()

    def initUI(self):
        # cria a área de filtros, vazia memo
        # cria a área de ações, atualizar consulta, adicionar, alterar e deletar
        # cria a área com a tabelona dos dado tudo
        # cria a área de paginação
        pass

    def get_table_model_instance(self) -> TableModelDefault:
        return TableModelDefault()
