from abc import abstractmethod
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon

from settings import FAV_ICON_FILE_NAME


class BaseWidget(QWidget):
    def __init__(
        self,
        title: str,
        width: int,
        height: int,
        parent=None,
        flags=Qt.WindowFlags(),
    ):
        super(BaseWidget, self).__init__(parent, flags)
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(FAV_ICON_FILE_NAME))
        self.resize(width, height)
        self._init_ui()

    @abstractmethod
    def _init_ui(self) -> None:
        raise NotImplementedError()
