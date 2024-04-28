from common.controller.base_change_controller import BaseChangeController
from routes.cliente.change.widget import ClienteChangeWidget
from routes.cliente.repository import ClienteRepository


class ClienteChangeController(BaseChangeController):
    _widget: ClienteChangeWidget
    _repository: ClienteRepository

    def _load_data(self) -> None:
        data = self._repository.find(self._data_id)
        if data:
            self._widget.nome_field.setText(data.get("nome"))
            self._widget.telefone_field.setText(data.get("telefone", ""))

            cidade_id = data.get("cidade_id")
            index = next(
                i
                for i in range(self._widget.cidade_field.count())
                if self._widget.cidade_field.itemData(i) == cidade_id
            )
            self._widget.cidade_field.setCurrentIndex(index)

    def _get_widget_instance(self) -> ClienteChangeWidget:
        return ClienteChangeWidget()

    def _get_repository_instance(self) -> ClienteRepository:
        return ClienteRepository()

    def execute_action(self) -> None:
        nome = self._widget.nome_field.text()
        cidade = self._widget.cidade_field.currentData()
        telefone = self._widget.telefone_field.text() or None
        if not nome:
            self._widget.show_info_pop_up("Atenção", "O nome do cliente é obrigatório")
        elif self._repository.change(
            self._data_id,
            {"nome": nome.strip(), "cidade_id": cidade, "telefone": telefone.strip()},
        ):
            self._widget.show_info_pop_up("Sucesso", "Cliente alterado com sucesso")
            self._caller.update_table_data()
            self._widget.close()
        else:
            self._widget.show_error_pop_up(
                "Erro",
                "Erro ao alterar o cliente",
                "Por favor, entre em contato com o suporte",
            )
