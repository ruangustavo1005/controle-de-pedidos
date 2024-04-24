from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget


class BaseWidget(QWidget):
    def __init__(
        self,
        title: str,
        width: int = 800,
        height: int = 800,
        parent=None,
        flags=Qt.WindowFlags(),
    ):
        super(BaseWidget, self).__init__(parent, flags)
        # self.setWindowTitle(title)
        # self.setWindowIcon(QIcon(FAV_ICON_FILE_NAME))
        # self.headers = headers
        # self.resize(width, height)
        # self.base_layout = QVBoxLayout()
        # self._init_ui()
        # self.setLayout(self.base_layout)
