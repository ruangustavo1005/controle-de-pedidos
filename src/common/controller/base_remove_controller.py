from common.controller.base_crud_controller import BaseCRUDController
from common.controller.base_list_controller import BaseListController


class BaseRemoveController(BaseCRUDController):
    _data_id: int

    def __init__(self, data_id: int, caller: BaseListController | None = None) -> None:
        self._data_id = data_id
        self._caller = caller
        self._repository = self._get_repository_instance()

    def _get_widget_instance(self):
        return None
