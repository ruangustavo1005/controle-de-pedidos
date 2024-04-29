from PySide6.QtWidgets import QMessageBox

from common.controller.base_remove_controller import BaseRemoveController
from common.gui.widget.base_widget import BaseWidget
from routes.cliente.repository import ClienteRepository


class ClienteRemoveController(BaseRemoveController):
    _repository: ClienteRepository

    def _get_repository_instance(self) -> ClienteRepository:
        return ClienteRepository()

    def execute_action(self) -> None:
        if self._repository.count_pedidos(self._data_id) == 0:
            option = BaseWidget.show_question_pop_up(
                "Atenção",
                "Deseja remover a Cliente selecionado?",
                "Essa ação não pode ser desfeita!",
            )
            if option == QMessageBox.StandardButton.Ok:
                if self._repository.remove(self._data_id):
                    BaseWidget.show_info_pop_up(
                        "Sucesso", "Cliente removido com sucesso"
                    )
                    self._caller.update_table_data()
                else:
                    BaseWidget.show_error_pop_up(
                        "Erro",
                        "Erro ao excluir o cliente",
                        "Por favor, entre em contato com o suporte",
                    )
        else:
            BaseWidget.show_warning_pop_up(
                "Atenção",
                "Não é possível remover um cliente que possua pedidos relacionados!",
            )
