from typing import List

from PySide6.QtCore import QDateTime, QModelIndex, Qt
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import (
    QAbstractItemView,
    QDateTimeEdit,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableView,
    QVBoxLayout,
)

from common.gui.core.table_model_default import TableModelDefault
from common.gui.field.combo_box import ComboBox
from common.gui.widget.base_crud_widget import BaseCRUDWidget
from common.utils.currency import CurrencyUtils
from routes.cliente.repository import ClienteRepository
from routes.pedido.enum import PedidoStatusEnum
from routes.produto.repository import ProdutoRepository


class PedidoAddWidget(BaseCRUDWidget):
    def __init__(
        self,
        title: str = "Adicionar Pedido",
        width: int = 600,
        height: int = 600,
        parent=None,
        flags=Qt.WindowFlags(),
    ):
        self.table_produtos_data: dict[str, List] = {}
        super().__init__(title, width, height, parent, flags)

    def _create_form_fields(self) -> QVBoxLayout:
        base_layout = QVBoxLayout()
        base_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        base_layout.addLayout(self.__create_data_status_cliente_area())
        base_layout.addWidget(self.__create_produto_area())

        return base_layout

    def __create_data_status_cliente_area(self) -> QHBoxLayout:
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        data_hora_label = QLabel("Data de Hora:")
        data_hora_label.setFixedWidth(75)
        layout.addWidget(data_hora_label)

        self.data_hora_field = QDateTimeEdit()
        self.data_hora_field.setDateTime(QDateTime.currentDateTime())
        self.data_hora_field.setFixedWidth(120)
        self.data_hora_field.setCalendarPopup(True)
        layout.addWidget(self.data_hora_field)

        status_label = QLabel("Status:")
        status_label.setFixedWidth(40)
        layout.addWidget(status_label)

        self.status_field = ComboBox()
        self.status_field.setFixedWidth(100)
        for enum in PedidoStatusEnum:
            self.status_field.addItem(enum.description, enum.value)
        self.status_field.setCurrentIndexByData(PedidoStatusEnum.EM_PRODUCAO.value)
        layout.addWidget(self.status_field)

        cliente_label = QLabel("Cliente:")
        cliente_label.setFixedWidth(45)
        layout.addWidget(cliente_label)

        self.cliente_field = ComboBox()
        self.cliente_field.setFixedWidth(180)
        self.cliente_field.addItem("", None)
        cliente_repository = ClienteRepository()
        for cliente in cliente_repository.list_for_combo_box(
            desc_column="nome", id_column="id"
        ):
            self.cliente_field.addItem(cliente["nome"], cliente["id"])
        layout.addWidget(self.cliente_field)

        return layout

    def __create_produto_area(self) -> QGroupBox:
        layout = QVBoxLayout()

        product_to_add_layout = QHBoxLayout()
        product_to_add_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self._produto_label = QLabel("Produto:")
        self._produto_label.setFixedWidth(50)
        product_to_add_layout.addWidget(self._produto_label)

        self._produto_to_add_field = ComboBox()
        self._produto_to_add_field.setFixedWidth(180)
        self._produto_to_add_field.addItem("", None)
        produto_repository = ProdutoRepository()
        for produto in produto_repository.list_for_combo_box():
            self._produto_to_add_field.addItem(
                produto["nome"],
                {
                    "id": produto["id"],
                    "nome": produto["nome"],
                    "preco": produto["preco"],
                },
            )
        product_to_add_layout.addWidget(self._produto_to_add_field)

        self._qtd_label = QLabel("Qtd.:")
        self._qtd_label.setFixedWidth(25)
        product_to_add_layout.addWidget(self._qtd_label)

        self._qtd_to_add_field = QLineEdit()
        self._qtd_to_add_field.setValidator(QIntValidator())
        self._qtd_to_add_field.setFixedWidth(40)
        product_to_add_layout.addWidget(self._qtd_to_add_field)

        self._add_produto_button = QPushButton("Adicionar")
        self._add_produto_button.setFixedWidth(100)
        self._add_produto_button.clicked.connect(self.__add_produto_button_clicked)
        product_to_add_layout.addWidget(self._add_produto_button)

        layout.addLayout(product_to_add_layout)

        self.table_produtos = QTableView()
        self.table_produtos.resizeRowsToContents()
        self.table_produtos.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.table_produtos.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )
        self.table_model_produtos = TableModelDefault(
            ["ID", "Nome", "Qtd.", "Preço (float)", "Preço", "Subtotal"]
        )
        self.table_produtos.setModel(self.table_model_produtos)
        self.table_produtos.setColumnWidth(0, 30)
        self.table_produtos.setColumnWidth(1, 200)
        self.table_produtos.setColumnWidth(2, 40)
        self.table_produtos.setColumnWidth(4, 70)
        self.table_produtos.setColumnWidth(5, 70)
        self.table_produtos.hideColumn(3)
        self.table_produtos.doubleClicked.connect(self.__table_produto_double_clicked)

        layout.addWidget(self.table_produtos)

        table_footer_options_layout = QHBoxLayout()

        self._double_click_label = QLabel(
            "<b>* Duplo clique no item da tabela para removê-lo</b>"
        )
        self._double_click_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        table_footer_options_layout.addWidget(self._double_click_label)

        valor_total_pedido_label = QLabel("<b>Total:</b>")
        valor_total_pedido_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        table_footer_options_layout.addWidget(valor_total_pedido_label)

        self.__valor_total_pedido_field = QLineEdit()
        self.__valor_total_pedido_field.setReadOnly(True)
        self.__valor_total_pedido_field.setFixedWidth(80)
        self.__valor_total_pedido_field.setAlignment(Qt.AlignmentFlag.AlignRight)
        table_footer_options_layout.addWidget(self.__valor_total_pedido_field)

        layout.addLayout(table_footer_options_layout)

        group = QGroupBox("Produtos")
        group.setLayout(layout)
        return group

    def __add_produto_button_clicked(self) -> None:
        produto: dict = self._produto_to_add_field.currentData()
        quantidade = int(self._qtd_to_add_field.text() or 0)

        if produto and quantidade:
            id_produto = produto.get("id")

            if self.table_produtos_data.get(id_produto):
                self.table_produtos_data[id_produto][2] += quantidade
            else:
                self.table_produtos_data[id_produto] = [
                    produto.get("id"),
                    produto.get("nome"),
                    quantidade,
                    produto.get("preco"),
                    CurrencyUtils.float_to_view(produto.get("preco")),
                    None,
                ]

            subtotal = (
                self.table_produtos_data.get(id_produto)[2]
                * self.table_produtos_data.get(id_produto)[3]
            )
            self.table_produtos_data[id_produto][5] = CurrencyUtils.float_to_view(
                subtotal
            )

            self.update_table_produto_values()

            self._produto_to_add_field.setCurrentIndex(0)
            self._qtd_to_add_field.setText("")

    def __table_produto_double_clicked(self, index: QModelIndex) -> None:
        id_produto = index.siblingAtColumn(0).data()
        del self.table_produtos_data[id_produto]
        self.update_table_produto_values()

    def update_table_produto_values(self) -> None:
        self.table_model_produtos.setData(list(self.table_produtos_data.values()))
        self.__update_valor_total_pedido()

    def __update_valor_total_pedido(self) -> None:
        total = sum([item[2] * item[3] for item in self.table_produtos_data.values()])
        self.__valor_total_pedido_field.setText(CurrencyUtils.float_to_view(total))
