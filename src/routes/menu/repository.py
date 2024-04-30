import sqlite3
from typing import Any, List

from common.repository.base_repository import BaseRepository
from routes.pedido.enum import PedidoStatusEnum
from routes.produto.enum import ProdutoUnidadeMedidaEnum


class MenuRepository(BaseRepository):
    def _get_table_name(self) -> str:
        return "pedido_produto"

    def list(
        self,
        page: int,
        limit: int = 20,
        columns: str = "*",
        order: str = "1 ASC",
        filter: str = "1 = 1",
    ) -> List[List[Any]]:
        offset = (page - 1) * limit

        sql = f"""
SELECT produto.id AS produto_id,
       produto.nome AS produto_nome,
       REPLACE(SUM(pedido_produto.quantidade) || " " || {self._build_case_from_enum("produto.unidade_medida", ProdutoUnidadeMedidaEnum)}, '.', ',') AS quantidade
  FROM pedido_produto
  JOIN produto
    ON produto.id = pedido_produto.produto_id
  JOIN pedido
    ON pedido.id = pedido_produto.pedido_id
  JOIN cliente
    ON cliente.id = pedido.cliente_id
  JOIN cidade
    ON cidade.id = cliente.cidade_id
 WHERE pedido.status = ? AND {filter}
 GROUP BY 1, 2
 ORDER BY 2
 LIMIT ?
OFFSET ?;
        """

        cursor = self._get_connection().cursor()
        cursor.execute(sql, (PedidoStatusEnum.EM_PRODUCAO.value, limit, offset))
        results = cursor.fetchall()

        items = [list(row) for row in results]

        cursor.close()
        return items

    def count(self, filter: str = "1 = 1") -> int:
        sql = """
WITH origin AS (
    SELECT produto.id AS produto_id
      FROM pedido_produto
      JOIN produto
        ON produto.id = pedido_produto.produto_id
      JOIN pedido
        ON pedido.id = pedido_produto.pedido_id
     WHERE pedido.status = ?
     GROUP BY 1
)

SELECT COUNT(1) AS count FROM origin;
        """

        cursor = self._get_connection().cursor()
        cursor.execute(sql, (PedidoStatusEnum.EM_PRODUCAO.value,))
        results: sqlite3.Row = cursor.fetchone()

        count = results["count"]

        cursor.close()
        return count
