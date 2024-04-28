from PySide6.QtCore import Qt

from routes.cidade.add.widget import CidadeAddWidget


class CidadeChangeWidget(CidadeAddWidget):
    def __init__(
        self,
        title: str = "Alterar Cidade",
        width: int = 300,
        height: int = 80,
        parent=None,
        flags=Qt.WindowFlags(),
    ):
        super().__init__(title, width, height, parent, flags)
