from abc import abstractmethod

from common.controller.base_crud_controller import BaseCRUDController
from common.controller.base_list_controller import BaseListController
from common.gui.widget.base_change_widget import BaseChangeWidget


class BaseChangeController(BaseCRUDController):
    _widget: BaseChangeWidget
    _data_id: int

    def __init__(self, data_id: int, caller: BaseListController | None = None) -> None:
        self._data_id = data_id
        super().__init__(caller)
        self._load_data()

    def _load_data() -> None:
        raise NotImplementedError()

    @abstractmethod
    def _get_widget_instance(self) -> BaseChangeWidget:
        raise NotImplementedError()
