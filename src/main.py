import sys
from PySide6.QtWidgets import QApplication

import database
from routes.cidade.list.controller import CidadeListController


database.create_if_not_exists()

app = QApplication(sys.argv)

controller = CidadeListController()
controller.show()

sys.exit(app.exec())
