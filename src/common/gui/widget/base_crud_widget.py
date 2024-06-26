from abc import abstractmethod

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QLayout, QPushButton, QVBoxLayout

from common.gui.widget.base_widget import BaseWidget


class BaseCRUDWidget(BaseWidget):
    def __init__(
        self,
        title: str,
        width: int = 400,
        height: int = 400,
        parent=None,
        flags=Qt.WindowFlags(),
    ):
        super().__init__(title, width, height, parent, flags)

    def _init_ui(self) -> None:
        self.base_layout = QVBoxLayout()

        self.form_fields_layout = self._create_form_fields()
        self.base_layout.addLayout(self.form_fields_layout)

        self.actions_area_layout = self._create_actions_area()
        self.base_layout.addLayout(self.actions_area_layout)

        self.setLayout(self.base_layout)

    @abstractmethod
    def _create_form_fields(self) -> QLayout:
        raise NotImplementedError()

    def _create_actions_area(self) -> QHBoxLayout:
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.submit_button = QPushButton("Confirmar")
        self.submit_button.setFixedWidth(100)
        layout.addWidget(self.submit_button)

        return layout
