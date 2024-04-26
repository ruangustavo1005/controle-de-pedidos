from PySide6.QtCore import Qt
from typing import Any, List
from PySide6.QtWidgets import QMenuBar
from PySide6.QtGui import QAction, QIcon

from common.gui.widget.base_list_widget import BaseListWidget
from settings import FAV_ICON_FILE_NAME


class MenuWidget(BaseListWidget):
    def __init__(
        self,
        title: str = "Controle de Pedidos",
        headers: List[List[Any]] = ["ID do Produto", "Produto", "Quantidade"],
        width: int = 800,
        height: int = 738,
        parent=None,
        flags=Qt.WindowFlags(),
    ):
        super().__init__(title, headers, width, height, parent, flags)
        self.table.hideColumn(0)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 75)

    def _init_ui(self) -> None:
        super()._init_ui()

        self.menu_bar = QMenuBar()
        self.routes_menu = self.menu_bar.addMenu("Cadastros")
        self.pedido_menu_item = QAction(
            text="Pedidos", icon=QIcon(FAV_ICON_FILE_NAME), parent=self
        )
        self.produto_menu_item = QAction(
            text="Produtos", icon=QIcon(FAV_ICON_FILE_NAME), parent=self
        )
        self.cliente_menu_item = QAction(
            text="Clientes", icon=QIcon(FAV_ICON_FILE_NAME), parent=self
        )
        self.cidade_menu_item = QAction(
            text="Cidades", icon=QIcon(FAV_ICON_FILE_NAME), parent=self
        )
        self.routes_menu.addActions(
            [
                self.pedido_menu_item,
                self.produto_menu_item,
                self.cliente_menu_item,
                self.cidade_menu_item,
            ]
        )
        self.base_layout.setMenuBar(self.menu_bar)

        self.add_button.hide()
        self.change_button.hide()
        self.remove_button.hide()
