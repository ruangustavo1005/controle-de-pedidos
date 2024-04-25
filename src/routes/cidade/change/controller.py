from common.controller.base_controller import BaseController
from common.controller.base_crud_controller import BaseCRUDController
from routes.cidade.change.widget import CidadeChangeWidget
from routes.cidade.repository import CidadeRepository


class CidadeChangeController(BaseCRUDController):
    _widget: CidadeChangeWidget
    _repository: CidadeRepository

    def __init__(self, cidade_id: int, caller: BaseController | None = None) -> None:
        self.__cidade_id = cidade_id
        super().__init__(caller)
        self.__load_data()

    def __load_data(self, ) -> None:
        data = self._repository.find(self.__cidade_id)
        if data:
            self._widget.nome_field.setText(data.get("nome"))

    def _get_widget_instance(self) -> CidadeChangeWidget:
        return CidadeChangeWidget()

    def _get_repository_instance(self) -> CidadeRepository:
        return CidadeRepository()

    def execute_action(self) -> None:
        nome = self._widget.nome_field.text()
        if not nome:
            self._widget.show_info_pop_up(
                "Atenção", "O nome da cidade é obrigatório"
            )
        elif self._repository.change(self.__cidade_id, {"nome": nome}):
            self._widget.show_info_pop_up(
                "Sucesso", "Cidade alterada com sucesso"
            )
            self._caller.update_table_data()
            self._widget.close()
        else:
            self._widget.show_error_pop_up(
                "Erro",
                "Erro ao alterar a cidade",
                "Por favor, entre em contato com o suporte",
            )
