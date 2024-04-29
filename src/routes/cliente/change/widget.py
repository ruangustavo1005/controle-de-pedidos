from PySide6.QtCore import Qt

from routes.cliente.add.widget import ClienteAddWidget


class ClienteChangeWidget(ClienteAddWidget):
    def __init__(
        self,
        title: str = "Alterar Cliente",
        width: int = 300,
        height: int = 130,
        parent=None,
        flags=Qt.WindowFlags(),
    ):
        super().__init__(title, width, height, parent, flags)
