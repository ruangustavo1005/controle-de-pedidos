from typing import Any, List
from common.gui.widget.base_list_widget import BaseListWidget
from PySide6.QtCore import Qt


class CidadeListWidget(BaseListWidget):
    def __init__(
        self,
        title: str = "Cidade",
        headers: List[List[Any]] = ["Nome", "Qtd. de Clientes"],
        width: int = 800,
        height: int = 738,
        parent=None,
        flags=Qt.WindowFlags(),
    ):
        super().__init__(title, headers, width, height, parent, flags)
