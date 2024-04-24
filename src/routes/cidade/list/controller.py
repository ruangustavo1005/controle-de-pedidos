from common.controller.base_controller import BaseController
from common.controller.base_list_controller import BaseListController
from routes.cidade.add.controller import CidadeAddController
from routes.cidade.list.widget import CidadeListWidget
from routes.cidade.repository import CidadeRepository


class CidadeListController(BaseListController):
    _widget: CidadeListWidget
    _repository: CidadeRepository

    def __init__(
        self, rows_per_page: int = 20, caller: BaseController | None = None
    ) -> None:
        super().__init__(rows_per_page, caller)

    def _get_widget_instance(self) -> CidadeListWidget:
        return CidadeListWidget()

    def _get_repository_instance(self) -> CidadeRepository:
        return CidadeRepository()

    def _set_widget_connections(self) -> None:
        super()._set_widget_connections()
        self._widget.add_button.clicked.connect(self.__add_button_clicked)

    def __add_button_clicked(self) -> None:
        self.add_controller = CidadeAddController(self)
        self.add_controller.show()
