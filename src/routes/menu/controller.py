from common.controller.base_list_controller import BaseListController
from routes.menu.repository import MenuRepository
from routes.menu.widget import MenuWidget


class MenuController(BaseListController):
    _widget: MenuWidget
    _repository: MenuRepository
    
    def _get_widget_instance(self) -> MenuWidget:
        return MenuWidget()
    
    def _get_repository_instance(self) -> MenuRepository:
        return MenuRepository()
