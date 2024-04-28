from common.controller.base_crud_controller import BaseCRUDController
from routes.produto.add.widget import ProdutoAddWidget
from routes.produto.repository import ProdutoRepository


class ProdutoAddController(BaseCRUDController):
    _widget: ProdutoAddWidget
    _repository: ProdutoRepository

    def _get_widget_instance(self) -> ProdutoAddWidget:
        return ProdutoAddWidget()

    def _get_repository_instance(self) -> ProdutoRepository:
        return ProdutoRepository()

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
