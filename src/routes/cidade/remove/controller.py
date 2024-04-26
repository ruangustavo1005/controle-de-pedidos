from PySide6.QtWidgets import QMessageBox

from common.controller.base_remove_controller import BaseRemoveController
from common.gui.widget.base_widget import BaseWidget
from routes.cidade.repository import CidadeRepository


class CidadeRemoveController(BaseRemoveController):
    _repository: CidadeRepository

    def _get_repository_instance(self) -> CidadeRepository:
        return CidadeRepository()

    def execute_action(self) -> None:
        print("count", self._repository.count_clientes(self._data_id))
        if self._repository.count_clientes(self._data_id) == 0:
            print("count ok")
            option = BaseWidget.show_question_pop_up(
                "Atenção",
                "Deseja remove a Cidade selecionada?",
                "Essa ação não pode ser desfeita!",
            )
            if option == QMessageBox.StandardButton.Ok:
                if self._repository.remove(self._data_id):
                    BaseWidget.show_info_pop_up(
                        "Sucesso", "Cidade removida com sucesso"
                    )
                    self._caller.update_table_data()
                else:
                    BaseWidget.show_error_pop_up(
                        "Erro",
                        "Erro ao excluir a cidade",
                        "Por favor, entre em contato com o suporte",
                    )
        else:
            BaseWidget.show_warning_pop_up(
                "Atenção",
                "Não é possível remover uma cidade que possua clientes relacionados!",
            )
