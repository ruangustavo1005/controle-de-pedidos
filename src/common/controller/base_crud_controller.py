from abc import abstractmethod

from common.controller.base_controller import BaseController
from common.controller.base_list_controller import BaseListController
from common.gui.widget.base_crud_widget import BaseCRUDWidget


class BaseCRUDController(BaseController):
    _widget: BaseCRUDWidget
    _caller: BaseListController

    def __init__(self, caller: BaseController | None = None) -> None:
        super().__init__(caller)
        self._widget.submit_button.clicked.connect(self.execute_action)

    @abstractmethod
    def _get_widget_instance(self) -> BaseCRUDWidget:
        raise NotImplementedError()

    @abstractmethod
    def execute_action(self) -> None:
        raise NotImplementedError()
