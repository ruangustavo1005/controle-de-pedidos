from PySide6.QtWidgets import QMessageBox

from common.controller.base_list_controller import BaseListController
from common.controller.base_remove_controller import BaseRemoveController
from common.gui.widget.base_widget import BaseWidget
from routes.pedido.repository import PedidoRepository


class PedidoRemoveController(BaseRemoveController):
    _repository: PedidoRepository

    def _get_repository_instance(self) -> PedidoRepository:
        return PedidoRepository()

    def execute_action(self) -> None:
        option = BaseWidget.show_question_pop_up(
            "Atenção",
            "Deseja remover o Pedido selecionado?",
            "Essa ação não pode ser desfeita!",
        )
        if option == QMessageBox.StandardButton.Ok:
            if self._repository.remove(self._data_id):
                BaseWidget.show_info_pop_up("Sucesso", "Pedido removido com sucesso")
                self._caller.update_table_data()
                if isinstance(self._caller._caller, BaseListController):
                    self._caller._caller.update_table_data()
            else:
                BaseWidget.show_error_pop_up(
                    "Erro",
                    "Erro ao excluir o pedido",
                    "Por favor, entre em contato com o suporte",
                )
