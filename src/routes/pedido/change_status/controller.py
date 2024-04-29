from common.controller.base_change_controller import BaseChangeController
from common.controller.base_list_controller import BaseListController
from routes.pedido.change_status.widget import PedidoStatusChangeWidget
from routes.pedido.repository import PedidoRepository


class PedidoStatusChangeController(BaseChangeController):
    _widget: PedidoStatusChangeWidget
    _repository: PedidoRepository

    def _load_data(self) -> None:
        data = self._repository.find(self._data_id)
        if data:
            self._widget.status_field.setCurrentIndexByData(data.get("status"))

    def _get_widget_instance(self) -> PedidoStatusChangeWidget:
        return PedidoStatusChangeWidget()

    def _get_repository_instance(self) -> PedidoRepository:
        return PedidoRepository()

    def execute_action(self) -> None:
        status = self._widget.status_field.currentData()
        if self._repository.change(self._data_id, {"status": status}):
            self._widget.show_info_pop_up(
                "Sucesso", "Status do pedido alterado com sucesso"
            )
            self._caller.update_table_data()
            if isinstance(self._caller._caller, BaseListController):
                self._caller._caller.update_table_data()
            self._widget.close()
        else:
            self._widget.show_error_pop_up(
                "Erro",
                "Erro ao alterar o status do pedido",
                "Por favor, entre em contato com o suporte",
            )
