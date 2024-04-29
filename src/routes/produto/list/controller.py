from common.controller.base_controller import BaseController
from common.controller.base_list_controller import BaseListController
from routes.cidade.change.controller import CidadeChangeController
from routes.produto.add.controller import ProdutoAddController
from routes.produto.list.widget import ProdutoListWidget
from routes.produto.remove.controller import ProdutoRemoveController
from routes.produto.repository import ProdutoRepository


class ProdutoListController(BaseListController):
    _widget: ProdutoListWidget
    _repository: ProdutoRepository

    def __init__(self, caller: BaseController | None = None) -> None:
        super().__init__(rows_per_page=20, caller=caller)

    def _get_widget_instance(self) -> ProdutoListWidget:
        return ProdutoListWidget()

    def _get_repository_instance(self) -> ProdutoRepository:
        return ProdutoRepository()

    def _build_list_filter(self) -> str:
        nome_filter = self._widget.nome_filter.text()
        if nome_filter:
            return f'UPPER(nome) LIKE UPPER("%{nome_filter}%")'
        return super()._build_list_filter()

    def _set_widget_connections(self) -> None:
        super()._set_widget_connections()
        self._widget.add_button.clicked.connect(self.__add_button_clicked)
        self._widget.change_button.clicked.connect(self.__change_button_clicked)
        self._widget.table.doubleClicked.connect(self.__change_button_clicked)
        self._widget.remove_button.clicked.connect(self.__remove_button_clicked)

    def __add_button_clicked(self) -> None:
        self.add_controller = ProdutoAddController(self)
        self.add_controller.show()

    def __change_button_clicked(self) -> None:
        cidade_id = int(self._selected_data[0])
        self.change_controller = CidadeChangeController(cidade_id, self)
        self.change_controller.show()

    def __remove_button_clicked(self) -> None:
        produto_id = int(self._selected_data[0])
        self.remove_controller = ProdutoRemoveController(produto_id, self)
        self.remove_controller.execute_action()
