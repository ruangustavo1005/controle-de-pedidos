from abc import abstractmethod
from common.controller.base_controller import BaseController
from common.gui.widget.base_crud_widget import BaseCRUDWidget


class BaseCRUDController(BaseController):
    _widget: BaseCRUDWidget

    @abstractmethod
    def _get_widget_instance(self) -> BaseCRUDWidget:
        raise NotImplementedError()
