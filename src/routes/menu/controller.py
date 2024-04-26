from common.controller.base_controller import BaseController
from common.controller.base_list_controller import BaseListController
from routes.cidade.list.controller import CidadeListController
from routes.menu.repository import MenuRepository
from routes.menu.widget import MenuWidget


class MenuController(BaseListController):
    _widget: MenuWidget
    _repository: MenuRepository

    def __init__(self, caller: BaseController | None = None) -> None:
        super().__init__(rows_per_page=20, caller=caller)

    def _set_widget_connections(self) -> None:
        super()._set_widget_connections()
        self._widget.cidade_menu_item.triggered.connect(
            self.__cidade_menu_item_triggered
        )

    def __cidade_menu_item_triggered(self) -> None:
        self.cidade_list_controller = CidadeListController(self)
        self.cidade_list_controller.show()

    def _get_widget_instance(self) -> MenuWidget:
        return MenuWidget()

    def _get_repository_instance(self) -> MenuRepository:
        return MenuRepository()
