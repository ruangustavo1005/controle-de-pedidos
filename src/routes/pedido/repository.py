# flake8: noqa: E501
import sqlite3
from typing import Any, Dict, List

from common.repository.base_repository import BaseRepository
from routes.pedido.enum import PedidoStatusEnum


class PedidoRepository(BaseRepository):
    def _get_table_name(self) -> str:
        return "pedido"

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
SELECT pedido.id,
       STRFTIME('%d/%m/%Y %H:%M', pedido.data_hora) AS data_hora,
       cliente.nome AS cliente,
       cidade.nome AS cidade,
       {self._build_case_from_enum('pedido.status', PedidoStatusEnum, 'status')},
       REPLACE(PRINTF('R$ %.2f', SUM(pedido_produto.quantidade * pedido_produto.preco_unitario)), '.', ',') AS valor_total
  FROM pedido
  JOIN cliente
    ON cliente.id = pedido.cliente_id
  JOIN cidade
    ON cidade.id = cliente.cidade_id
  JOIN pedido_produto
    ON pedido_produto.pedido_id = pedido.id
 WHERE {filter}
 GROUP BY 1, 2, 3, 4, 5
 ORDER BY 2 DESC
 LIMIT ?
 OFFSET ?
        """

        cursor = self._get_connection().cursor()
        cursor.execute(sql, (limit, offset))
        results = cursor.fetchall()

        items = [list(row) for row in results]

        cursor.close()
        return items

    def count(self, filter: str = "1 = 1") -> int:
        sql = f"""
SELECT COUNT(1) AS count
  FROM pedido
  JOIN cliente
    ON cliente.id = pedido.cliente_id
  JOIN cidade
    ON cidade.id = cliente.cidade_id
 WHERE {filter}
        """

        cursor = self._get_connection().cursor()
        cursor.execute(sql)
        results: sqlite3.Row = cursor.fetchone()

        count = results["count"]

        cursor.close()
        return count

    def add(
        self,
        data_hora: str,
        status: str,
        cliente_id: int,
        produtos: List[Dict[str, Any]],
    ) -> bool:
        try:
            cursor = self._get_connection().cursor()

            sql = f"INSERT INTO {self._table_name} (data_hora, status, cliente_id) VALUES (?, ?, ?)"
            cursor.execute(sql, (data_hora, status, cliente_id))

            id_pedido = cursor.lastrowid

            for produto in produtos:
                sql = "INSERT INTO pedido_produto (pedido_id, produto_id, quantidade, preco_unitario) VALUES (?, ?, ?, ?)"
                cursor.execute(sql, (id_pedido, produto[0], produto[2], produto[3]))

            self._get_connection().commit()
            cursor.close()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}")
            return False

    def find(self, id: int) -> Dict | None:
        sql = """
SELECT pedido.data_hora,
       pedido.status,
       pedido.cliente_id,
       json_group_object(
           produto.id,
           json_array(
               produto.id,
               produto.nome,
               pedido_produto.quantidade,
               pedido_produto.preco_unitario,
               REPLACE(PRINTF('R$ %.2f', pedido_produto.preco_unitario), '.', ','),
               REPLACE(PRINTF('R$ %.2f', pedido_produto.quantidade * pedido_produto.preco_unitario), '.', ',')
           )
       ) AS produtos
  FROM pedido
  JOIN pedido_produto
    ON pedido_produto.pedido_id = pedido.id
  JOIN produto
    ON produto.id = pedido_produto.produto_id
 WHERE pedido.id = ?
 GROUP BY 1, 2, 3
        """

        cursor = self._get_connection().cursor()
        cursor.execute(sql, (id,))
        result = cursor.fetchone()

        dict_result = dict(result) if result is not None else None

        cursor.close()
        return dict_result

    def remove(self, id: int) -> bool:
        try:
            cursor = self._get_connection().cursor()

            sql = f"DELETE FROM {self._table_name} WHERE id = ?"
            cursor.execute(sql, (id,))

            sql = f"DELETE FROM pedido_produto WHERE pedido_id = ?"
            cursor.execute(sql, (id,))

            self._get_connection().commit()
            cursor.close()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao remover dados: {e}")
            return False
