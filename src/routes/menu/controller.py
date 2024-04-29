from common.controller.base_controller import BaseController
from common.controller.base_list_controller import BaseListController
from routes.cidade.list.controller import CidadeListController
from routes.cliente.list.controller import ClienteListController
from routes.menu.repository import MenuRepository
from routes.menu.widget import MenuWidget
from routes.pedido.list.controller import PedidoListController
from routes.produto.list.controller import ProdutoListController


class MenuController(BaseListController):
    _widget: MenuWidget
    _repository: MenuRepository

    def __init__(self, caller: BaseController | None = None) -> None:
        super().__init__(rows_per_page=20, caller=caller)

    def _build_list_filter(self) -> str:
        cidade_id_filter = self._widget.cidade_filter.currentData()
        if cidade_id_filter:
            return f"cidade.id = {cidade_id_filter}"
        return super()._build_list_filter()

    def _set_widget_connections(self) -> None:
        super()._set_widget_connections()
        self._widget.cidade_menu_item.triggered.connect(
            self.__cidade_menu_item_triggered
        )
        self._widget.cliente_menu_item.triggered.connect(
            self.__cliente_menu_item_triggered
        )
        self._widget.produto_menu_item.triggered.connect(
            self.__produto_menu_item_triggered
        )
        self._widget.pedido_menu_item.triggered.connect(
            self.__pedido_menu_item_triggered
        )

    def __cidade_menu_item_triggered(self) -> None:
        self.cidade_list_controller = CidadeListController(self)
        self.cidade_list_controller.show()

    def __cliente_menu_item_triggered(self) -> None:
        self.cliente_list_controller = ClienteListController(self)
        self.cliente_list_controller.show()

    def __produto_menu_item_triggered(self) -> None:
        self.produto_list_controller = ProdutoListController(self)
        self.produto_list_controller.show()

    def __pedido_menu_item_triggered(self) -> None:
        self.pedido_list_controller = PedidoListController(self)
        self.pedido_list_controller.show()

    def _get_widget_instance(self) -> MenuWidget:
        return MenuWidget()

    def _get_repository_instance(self) -> MenuRepository:
        return MenuRepository()
