import re
from common.controller.base_controller import BaseController
from common.controller.base_list_controller import BaseListController
from routes.cliente.add.controller import ClienteAddController
from routes.cliente.change.controller import ClienteChangeController
from routes.cliente.list.widget import ClienteListWidget
from routes.cliente.remove.controller import ClienteRemoveController
from routes.cliente.repository import ClienteRepository
from PySide6.QtGui import QDesktopServices
from PySide6.QtCore import QUrl


class ClienteListController(BaseListController):
    _widget: ClienteListWidget
    _repository: ClienteRepository

    def __init__(self, caller: BaseController | None = None) -> None:
        super().__init__(rows_per_page=20, caller=caller)

    def _get_widget_instance(self) -> ClienteListWidget:
        return ClienteListWidget()

    def _get_repository_instance(self) -> ClienteRepository:
        return ClienteRepository()

    def _build_list_filter(self) -> str:
        filters = []
        nome_filter = self._widget.nome_filter.text()
        if nome_filter:
            filters.append(f'UPPER(nome) LIKE UPPER("%{nome_filter}%")')
        cidade_id_filter = self._widget.cidade_filter.currentData()
        if cidade_id_filter:
            filters.append(f"cidade_id = {cidade_id_filter}")
        return " AND ".join(filters) if filters else super()._build_list_filter()

    def _set_widget_connections(self) -> None:
        super()._set_widget_connections()
        self._widget.add_button.clicked.connect(self.__add_button_clicked)
        self._widget.change_button.clicked.connect(self.__change_button_clicked)
        self._widget.table.doubleClicked.connect(self.__change_button_clicked)
        self._widget.remove_button.clicked.connect(self.__remove_button_clicked)
        self._widget.whatsapp_button.clicked.connect(self.__whatsapp_button_clicked)

    def __add_button_clicked(self) -> None:
        self.add_controller = ClienteAddController(self)
        self.add_controller.show()

    def __change_button_clicked(self) -> None:
        cliente_id = int(self._selected_data[0])
        self.change_controller = ClienteChangeController(cliente_id, self)
        self.change_controller.show()

    def __remove_button_clicked(self) -> None:
        cliente_id = int(self._selected_data[0])
        self.remove_controller = ClienteRemoveController(cliente_id, self)
        self.remove_controller.execute_action()

    def __whatsapp_button_clicked(self) -> None:
        phone = "".join(re.findall(r'\d+', self._selected_data[2]))
        QDesktopServices.openUrl(QUrl(f"https://web.whatsapp.com/send?phone={phone}"))
