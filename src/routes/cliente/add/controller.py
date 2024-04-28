from common.controller.base_crud_controller import BaseCRUDController
from routes.cliente.add.widget import ClienteAddWidget
from routes.cliente.repository import ClienteRepository


class ClienteAddController(BaseCRUDController):
    _widget: ClienteAddWidget
    _repository: ClienteRepository

    def _get_widget_instance(self) -> ClienteAddWidget:
        return ClienteAddWidget()

    def _get_repository_instance(self) -> ClienteRepository:
        return ClienteRepository()

    def execute_action(self) -> None:
        nome = self._widget.nome_field.text()
        cidade = self._widget.cidade_field.currentData()
        telefone = self._widget.telefone_field.text() or None
        if not nome:
            self._widget.show_info_pop_up("Atenção", "O nome do cliente é obrigatório")
        elif self._repository.add({"nome": nome.strip(), "cidade_id": cidade, "telefone": telefone.strip()}):
            self._widget.show_info_pop_up("Sucesso", "Cliente criado com sucesso")
            self._caller.update_table_data()
            self._widget.close()
        else:
            self._widget.show_error_pop_up(
                "Erro",
                "Erro ao criar o cliente",
                "Por favor, entre em contato com o suporte",
            )
