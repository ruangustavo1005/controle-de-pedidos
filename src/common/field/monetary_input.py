from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt


class MonetaryInput(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setText("0,00")
        self.setCursorPosition(0)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.text().isdigit():
            new_text = self.text().replace(",", "") + event.text()
            new_text = new_text.zfill(2)
            self.setText(f"{int(new_text[:-2] or "0")},{new_text[-2:]}")
        elif event.key() == Qt.Key_Backspace:
            new_text = self.text().replace(",", "")
            new_text = new_text[:-1] if len(new_text) > 1 else "0"
            new_text = new_text.zfill(2)
            self.setText(f"{int(new_text[:-2] or '0')},{new_text[-2:]}")
