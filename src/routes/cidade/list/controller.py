from common.controller.base_list_controller import BaseListController
from routes.cidade.list.widget import CidadeListWidget
from routes.cidade.repository import CidadeRepository


class CidadeListController(BaseListController):
    _widget: CidadeListWidget
    _repository: CidadeRepository

    def __init__(self, rows_per_page: int = 20) -> None:
        super().__init__(rows_per_page)

    def _get_widget_instance(self) -> CidadeListWidget:
        return CidadeListWidget()

    def _get_repository_instance(self) -> CidadeRepository:
        return CidadeRepository()
