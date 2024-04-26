import sys

from PySide6.QtWidgets import QApplication

import database
from routes.menu.controller import MenuController

database.create_if_not_exists()

app = QApplication(sys.argv)

menu_controller = MenuController()
menu_controller.show()

sys.exit(app.exec())
