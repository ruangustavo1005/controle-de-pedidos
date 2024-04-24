import sqlite3
from abc import ABC, abstractmethod
from typing import Any, Dict, List

from common.repository.connection import Connection


class BaseRepository(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._table_name = self._get_table_name()

    @abstractmethod
    def _get_table_name(self) -> str:
        raise NotImplementedError()

    def list(
        self,
        page: int,
        limit: int = 20,
        columns: str = "*",
        order: str = "1 ASC",
        filter: str = "1 = 1",
    ) -> List[List[Any]]:
        offset = (page - 1) * limit

        sql = f"SELECT {columns} FROM {self._table_name} WHERE {filter} ORDER BY {order} LIMIT ? OFFSET ?"

        cursor = self._get_connection().cursor()
        cursor.execute(sql, (limit, offset))
        results = cursor.fetchall()

        items = [list(row) for row in results]

        cursor.close()
        return items

    def count(self) -> int:
        sql = f"SELECT COUNT(1) AS count FROM {self._table_name}"

        cursor = self._get_connection().cursor()
        cursor.execute(sql)
        results: sqlite3.Row = cursor.fetchone()

        count = results["count"]

        cursor.close()
        return count

    def add(self, data: Dict[str, Any]) -> bool:
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?" for _ in data.values()])
        values = tuple(data.values())

        sql = f"INSERT INTO {self._table_name} ({columns}) VALUES ({placeholders})"
        try:
            cursor = self._get_connection().cursor()
            cursor.execute(sql, values)
            self._get_connection().commit()
            cursor.close()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}")
            return False

    def _get_connection(self) -> sqlite3.Connection:
        return Connection.get_connection()

    def _close_connection(self) -> None:
        Connection.close_connection()
