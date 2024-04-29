from common.controller.base_crud_controller import BaseCRUDController
from common.controller.base_list_controller import BaseListController
from routes.pedido.add.widget import PedidoAddWidget
from routes.pedido.repository import PedidoRepository


class PedidoAddController(BaseCRUDController):
    _widget: PedidoAddWidget
    _repository: PedidoRepository

    def _get_widget_instance(self) -> PedidoAddWidget:
        return PedidoAddWidget()

    def _get_repository_instance(self) -> PedidoRepository:
        return PedidoRepository()

    def execute_action(self) -> None:
        cliente_id = int(self._widget.cliente_field.currentData() or "0")
        if not cliente_id:
            self._widget.show_info_pop_up(
                "Atenção", "O cliente do pedido é obrigatório"
            )
            return

        produtos = list(self._widget.table_produtos_data.values())
        if len(produtos) <= 0:
            self._widget.show_info_pop_up(
                "Atenção", "O pedido deve ter pelo menos 1 produto relacionado"
            )
            return

        data_hora = self._widget.data_hora_field.dateTime().toString("yyyy-MM-dd HH:mm")
        status = str(self._widget.status_field.currentData())

        if self._repository.add(data_hora, status, cliente_id, produtos):
            self._widget.show_info_pop_up("Sucesso", "Pedido criado com sucesso")
            self._caller.update_table_data()
            if isinstance(self._caller._caller, BaseListController):
                self._caller._caller.update_table_data()
            self._widget.close()
        else:
            self._widget.show_error_pop_up(
                "Erro",
                "Erro ao criar o pedido",
                "Por favor, entre em contato com o suporte",
            )
