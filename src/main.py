
import sys
from PySide6.QtWidgets import QApplication
from dotenv import load_dotenv

from common.gui.widget.base_list_widget import BaseListWidget
import database


load_dotenv()

database.create_if_not_exists()

app = QApplication(sys.argv)

tela = BaseListWidget("teste", ["foo", "bar"])
tela.show()

sys.exit(app.exec())
