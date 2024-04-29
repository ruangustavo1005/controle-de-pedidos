from PySide6.QtCore import Qt

from routes.produto.add.widget import ProdutoAddWidget


class ProdutoChangeWidget(ProdutoAddWidget):
    def __init__(
        self,
        title: str = "Alterar Produto",
        width: int = 300,
        height: int = 120,
        parent=None,
        flags=Qt.WindowFlags(),
    ):
        super().__init__(title, width, height, parent, flags)
