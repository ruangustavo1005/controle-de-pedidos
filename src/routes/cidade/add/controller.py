from common.controller.base_crud_controller import BaseCRUDController
from routes.cidade.add.widget import CidadeAddWidget
from routes.cidade.repository import CidadeRepository


class CidadeAddController(BaseCRUDController):
    _widget: CidadeAddWidget
    _repository: CidadeRepository

    def _get_widget_instance(self) -> CidadeAddWidget:
        return CidadeAddWidget()

    def _get_repository_instance(self) -> CidadeRepository:
        return CidadeRepository()

    def execute_action(self) -> None:
        nome = self._widget.nome_field.text()
        if not nome:
            self._widget.show_info_pop_up("Atenção", "O nome da cidade é obrigatório")
        elif self._repository.add({"nome": nome.strip()}):
            self._widget.show_info_pop_up("Sucesso", "Cidade criada com sucesso")
            self._caller.update_table_data()
            self._widget.close()
        else:
            self._widget.show_error_pop_up(
                "Erro",
                "Erro ao criar a cidade",
                "Por favor, entre em contato com o suporte",
            )
