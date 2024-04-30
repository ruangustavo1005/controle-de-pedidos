import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

import database
from routes.menu.controller import MenuController
from settings import FAV_ICON_FILE_NAME

database.create_if_not_exists()

app = QApplication(sys.argv)
app.setWindowIcon(QIcon(FAV_ICON_FILE_NAME))

menu_controller = MenuController()
menu_controller.show()

sys.exit(app.exec())
