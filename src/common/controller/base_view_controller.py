from abc import abstractmethod

from common.controller.base_crud_controller import BaseCRUDController
from common.controller.base_list_controller import BaseListController
from common.gui.widget.base_view_widget import BaseViewWidget


class BaseViewController(BaseCRUDController):
    _widget: BaseViewWidget
    _data_id: int

    def __init__(self, data_id: int, caller: BaseListController | None = None) -> None:
        self._data_id = data_id
        super().__init__(caller)
        self._load_data()
        self._widget.submit_button.hide()

    def _load_data(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def _get_widget_instance(self) -> BaseViewWidget:
        raise NotImplementedError()

    def execute_action(self) -> None:
        pass
