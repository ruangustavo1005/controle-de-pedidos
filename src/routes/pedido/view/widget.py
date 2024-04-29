from PySide6.QtCore import Qt

from routes.pedido.add.widget import PedidoAddWidget


class PedidoViewWidget(PedidoAddWidget):
    def __init__(
        self,
        title: str = "Visualizer Pedido",
        width: int = 600,
        height: int = 600,
        parent=None,
        flags=Qt.WindowFlags(),
    ):
        super().__init__(title, width, height, parent, flags)

    def _init_ui(self) -> None:
        super()._init_ui()

        self.data_hora_field.setReadOnly(True)
        self.status_field.setDisabled(True)
        self.cliente_field.setDisabled(True)
        self._produto_label.hide()
        self._produto_to_add_field.hide()
        self._qtd_label.hide()
        self._qtd_to_add_field.hide()
        self._add_produto_button.hide()
        self.table_produtos.doubleClicked.disconnect()
        self._double_click_label.setDisabled(True)
