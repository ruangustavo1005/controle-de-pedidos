import sqlite3
from typing import Any, Dict, List

from common.repository.base_repository import BaseRepository


class ProdutoRepository(BaseRepository):
    def _get_table_name(self) -> str:
        return "produto"

    def list(
        self,
        page: int,
        limit: int = 20,
        columns: str = "*",
        order: str = "1 ASC",
        filter: str = "true",
    ) -> List[List[Any]]:
        columns = ", ".join(
            [
                "id",
                "nome",
                "REPLACE(PRINTF('R$ %.2f', preco), '.', ',') AS preco",
                "unidade_medida",
                f"(SELECT COUNT(1) FROM pedido_produto WHERE pedido_produto.produto_id = {self._table_name}.id) AS qtd_vendas",  # noqa: E501
            ]
        )
        order = "LOWER(nome) ASC"
        return super().list(page, limit, columns, order, filter)

    def count_pedidos(self, id: int) -> int:
        sql = "SELECT COUNT(1) AS count FROM pedido_produto WHERE pedido_produto.produto_id = ?"

        cursor = self._get_connection().cursor()
        cursor.execute(sql, (id,))
        results: sqlite3.Row = cursor.fetchone()

        count = results["count"]

        cursor.close()
        return count

    def list_for_combo_box(self) -> List[Dict[str, Any]]:
        sql = f"SELECT id, nome FROM {self._table_name} ORDER BY nome"

        cursor = self._get_connection().cursor()
        cursor.execute(sql)
        results = cursor.fetchall()

        cursor.close()
        return results
