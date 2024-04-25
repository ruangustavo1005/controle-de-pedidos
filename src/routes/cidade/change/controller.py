from common.controller.base_change_controller import BaseChangeController
from routes.cidade.change.widget import CidadeChangeWidget
from routes.cidade.repository import CidadeRepository


class CidadeChangeController(BaseChangeController):
    _widget: CidadeChangeWidget
    _repository: CidadeRepository

    def _load_data(self) -> None:
        data = self._repository.find(self._data_id)
        if data:
            self._widget.nome_field.setText(data.get("nome"))

    def _get_widget_instance(self) -> CidadeChangeWidget:
        return CidadeChangeWidget()

    def _get_repository_instance(self) -> CidadeRepository:
        return CidadeRepository()

    def execute_action(self) -> None:
        nome = self._widget.nome_field.text()
        if not nome:
            self._widget.show_info_pop_up("Atenção", "O nome da cidade é obrigatório")
        elif self._repository.change(self._data_id, {"nome": nome}):
            self._widget.show_info_pop_up("Sucesso", "Cidade alterada com sucesso")
            self._caller.update_table_data()
            self._widget.close()
        else:
            self._widget.show_error_pop_up(
                "Erro",
                "Erro ao alterar a cidade",
                "Por favor, entre em contato com o suporte",
            )
