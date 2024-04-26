import sqlite3
from typing import Any, List

from common.repository.base_repository import BaseRepository


class CidadeRepository(BaseRepository):
    def _get_table_name(self) -> str:
        return "cidade"

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
                f"(SELECT COUNT(1) FROM cliente WHERE cliente.cidade_id = {self._table_name}.id) as qtd_clientes",
            ]
        )
        order = "LOWER(nome) ASC"
        return super().list(page, limit, columns, order, filter)

    def count_clientes(self, id: int) -> int:
        sql = "SELECT COUNT(1) AS count FROM cliente WHERE cidade_id = ?"

        cursor = self._get_connection().cursor()
        cursor.execute(sql, (id,))
        results: sqlite3.Row = cursor.fetchone()

        count = results["count"]

        cursor.close()
        return count
