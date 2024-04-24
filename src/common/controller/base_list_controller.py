import math
from abc import abstractmethod

from common.controller.base_controller import BaseController
from common.gui.widget.base_list_widget import BaseListWidget


class BaseListController(BaseController):
    _widget: BaseListWidget

    def __init__(self, rows_per_page: int = 20) -> None:
        self._rows_per_page = rows_per_page
        super().__init__()
        self._set_widget_connections()

    @abstractmethod
    def _get_widget_instance(self) -> BaseListWidget:
        raise NotImplementedError()

    def _set_widget_connections(self) -> None:
        self._widget.update_button.clicked.connect(self._update_button_clicked)
        self._widget.page_field.returnPressed.connect(self._page_field_return_pressed)
        self._widget.first_page_button.clicked.connect(self._first_page_button_clicked)
        self._widget.before_page_button.clicked.connect(
            self._before_page_button_clicked
        )
        self._widget.after_page_button.clicked.connect(self._after_page_button_clicked)
        self._widget.last_page_button.clicked.connect(self._last_page_button_clicked)

    def _update_button_clicked(self) -> None:
        self._widget.page_field.setText("1")
        self.update_table_data()

    def _page_field_return_pressed(self) -> None:
        page = int(self._widget.page_field.text())
        if page > self._page_count:
            self._widget.page_field.setText(str(self._page_count))
        elif page < 1:
            self._widget.page_field.setText("1")
        self.update_table_data()

    def _first_page_button_clicked(self) -> None:
        self._widget.page_field.setText("1")
        self.update_table_data()

    def _before_page_button_clicked(self) -> None:
        page = int(self._widget.page_field.text())
        self._widget.page_field.setText(str(max(page - 1, 1)))
        self.update_table_data()

    def _after_page_button_clicked(self) -> None:
        page = int(self._widget.page_field.text())
        self._widget.page_field.setText(str(min(page + 1, self._page_count)))
        self.update_table_data()

    def _last_page_button_clicked(self) -> None:
        self._widget.page_field.setText(str(self._page_count))
        self.update_table_data()

    def show(self) -> None:
        self.update_table_data()
        self._widget.show()

    def update_table_data(self) -> None:
        self._update_row_count()
        self._update_page_count()
        data = self._repository.list(
            page=int(self._widget.page_field.text()), limit=self._rows_per_page
        )
        self._widget.table_model.setData(data)

    def _update_row_count(self) -> None:
        self._row_count = self._repository.count()
        self._widget.set_row_count(self._row_count)

    def _update_page_count(self) -> None:
        self._page_count = math.ceil(self._row_count / self._rows_per_page)
        self._widget.set_page_count(self._page_count)
