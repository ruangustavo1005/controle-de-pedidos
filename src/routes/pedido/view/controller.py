import json

from PySide6.QtCore import QDateTime

from common.controller.base_view_controller import BaseViewController
from routes.pedido.repository import PedidoRepository
from routes.pedido.view.widget import PedidoViewWidget


class PedidoViewController(BaseViewController):
    _widget: PedidoViewWidget
    _repository: PedidoRepository

    def _load_data(self) -> None:
        data = self._repository.find(self._data_id)
        if data:
            data_hora = data.get("data_hora")
            format = "yyyy-MM-dd HH:mm"
            base_year = int(data_hora[:4])
            self._widget.data_hora_field.setDateTime(
                QDateTime.fromString(data_hora, format, base_year)
            )
            self._widget.status_field.setCurrentIndexByData(data.get("status"))
            self._widget.cliente_field.setCurrentIndexByData(data.get("cliente_id"))
            self._widget.table_produtos_data = json.loads(data.get("produtos"))
            self._widget.update_table_produto_values()

    def _get_widget_instance(self) -> PedidoViewWidget:
        return PedidoViewWidget()

    def _get_repository_instance(self) -> PedidoRepository:
        return PedidoRepository()
