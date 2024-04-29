from common.controller.base_change_controller import BaseChangeController
from routes.produto.change.widget import ProdutoChangeWidget
from routes.produto.repository import ProdutoRepository


class ProdutoChangeController(BaseChangeController):
    _widget: ProdutoChangeWidget
    _repository: ProdutoRepository

    def _load_data(self) -> None:
        data = self._repository.find(self._data_id)
        if data:
            self._widget.nome_field.setText(data.get("nome"))
            self._widget.preco_field.setValueFromFloat(data.get("preco"))
            self._widget.unidade_medida_field.setCurrentIndexByData(
                data.get("unidade_medida")
            )

    def _get_widget_instance(self) -> ProdutoChangeWidget:
        return ProdutoChangeWidget()

    def _get_repository_instance(self) -> ProdutoRepository:
        return ProdutoRepository()

    def execute_action(self) -> None:
        nome = self._widget.nome_field.text()
        preco = self._widget.preco_field.valueAsFloat()
        unidade_medida = self._widget.unidade_medida_field.currentData()
        if not nome:
            self._widget.show_info_pop_up("Atenção", "O nome do produto é obrigatório")
            return
        if preco == 0:
            self._widget.show_info_pop_up("Atenção", "O preço do produto é obrigatório")
            return
        elif self._repository.change(
            self._data_id,
            {"nome": nome.strip(), "preco": preco, "unidade_medida": unidade_medida},
        ):
            self._widget.show_info_pop_up("Sucesso", "Produto alterado com sucesso")
            self._caller.update_table_data()
            self._widget.close()
        else:
            self._widget.show_error_pop_up(
                "Erro",
                "Erro ao alterar o produto",
                "Por favor, entre em contato com o suporte",
            )
