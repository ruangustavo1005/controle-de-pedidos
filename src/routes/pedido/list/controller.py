from common.controller.base_controller import BaseController
from common.controller.base_list_controller import BaseListController
from routes.pedido.add.controller import PedidoAddController
from routes.pedido.change_status.controller import PedidoStatusChangeController
from routes.pedido.list.widget import PedidoListWidget
from routes.pedido.remove.controller import PedidoRemoveController
from routes.pedido.repository import PedidoRepository
from routes.pedido.view.controller import PedidoViewController


class PedidoListController(BaseListController):
    _widget: PedidoListWidget
    _repository: PedidoRepository

    def __init__(self, caller: BaseController | None = None) -> None:
        super().__init__(rows_per_page=20, caller=caller)

    def _get_widget_instance(self) -> PedidoListWidget:
        return PedidoListWidget()

    def _get_repository_instance(self) -> PedidoRepository:
        return PedidoRepository()

    def _build_list_filter(self) -> str:
        filters = []
        cliente_filter = self._widget.cliente_filter.text()
        if cliente_filter:
            filters.append(f"UPPER(cliente.nome) LIKE UPPER('%{cliente_filter}%')")
        cidade_id_filter = self._widget.cidade_filter.currentData()
        if cidade_id_filter:
            filters.append(f"cidade.id = {cidade_id_filter}")
        status_filter = self._widget.status_filter.currentData()
        if status_filter:
            filters.append(f"pedido.status = '{status_filter}'")
        return " AND ".join(filters) if filters else super()._build_list_filter()

    def _set_widget_connections(self) -> None:
        super()._set_widget_connections()
        self._widget.add_button.clicked.connect(self.__add_button_clicked)
        self._widget.remove_button.clicked.connect(self.__remove_button_clicked)
        self._widget.change_status_button.clicked.connect(
            self.__change_status_button_clicked
        )
        self._widget.view_button.clicked.connect(self.__view_button_clicked)
        self._widget.table.doubleClicked.connect(self.__view_button_clicked)

    def __add_button_clicked(self) -> None:
        self.add_controller = PedidoAddController(self)
        self.add_controller.show()

    def __remove_button_clicked(self) -> None:
        pedido_id = int(self._selected_data[0])
        self.view_controller = PedidoRemoveController(pedido_id, self)
        self.view_controller.execute_action()

    def __change_status_button_clicked(self) -> None:
        pedido_id = int(self._selected_data[0])
        self.change_status_controller = PedidoStatusChangeController(pedido_id, self)
        self.change_status_controller.show()

    def __view_button_clicked(self) -> None:
        pedido_id = int(self._selected_data[0])
        self.view_controller = PedidoViewController(pedido_id, self)
        self.view_controller.show()
