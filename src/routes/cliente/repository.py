import sqlite3
from typing import Any, List

from common.repository.base_repository import BaseRepository


class ClienteRepository(BaseRepository):
    def _get_table_name(self) -> str:
        return "cliente"

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
                "telefone",
                f"(SELECT cidade.nome FROM cidade WHERE cidade.id = {self._table_name}.cidade_id) AS nome_cidade",
                f"(SELECT COUNT(1) FROM pedido WHERE pedido.cliente_id = {self._table_name}.id) AS qtd_pedidos",
            ]
        )
        order = "LOWER(nome) ASC"
        return super().list(page, limit, columns, order, filter)

    def count_pedidos(self, id: int) -> int:
        sql = "SELECT COUNT(1) AS count FROM pedido WHERE cliente_id = ?"

        cursor = self._get_connection().cursor()
        cursor.execute(sql, (id,))
        results: sqlite3.Row = cursor.fetchone()

        count = results["count"]

        cursor.close()
        return count
