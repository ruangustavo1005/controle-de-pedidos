from abc import abstractmethod
from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QMessageBox

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

    def show_info_pop_up(
        cls, title: str, text: str, info_text: Optional[str] = None
    ) -> QMessageBox.StandardButton:
        cls.show_pop_up(title, text, QMessageBox.Icon.Information, info_text)

    def show_warning_pop_up(
        cls, title: str, text: str, info_text: Optional[str] = None
    ) -> QMessageBox.StandardButton:
        cls.show_pop_up(title, text, QMessageBox.Icon.Warning, info_text)

    def show_error_pop_up(
        cls, title: str, text: str, info_text: Optional[str] = None
    ) -> QMessageBox.StandardButton:
        cls.show_pop_up(title, text, QMessageBox.Icon.Critical, info_text)

    def show_question_pop_up(
        cls, title: str, text: str, info_text: Optional[str] = None
    ) -> QMessageBox.StandardButton:
        cls.show_pop_up(title, text, QMessageBox.Icon.Question, info_text)

    @classmethod
    def show_pop_up(
        cls,
        title: str,
        text: str,
        icon: QMessageBox.Icon,
        info_text: Optional[str] = None,
    ) -> QMessageBox.StandardButton:
        pop_up = QMessageBox()
        pop_up.setWindowTitle(title)
        pop_up.setText(text)
        pop_up.setIcon(icon)
        if info_text:
            pop_up.setInformativeText(info_text)

        pop_up.setStandardButtons(
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel
        )

        return pop_up.exec()
