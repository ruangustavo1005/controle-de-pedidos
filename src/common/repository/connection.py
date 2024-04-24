import sqlite3

from settings import DB_FILE_NAME


class Connection:
    __connection: sqlite3.Connection = None

    @classmethod
    def get_connection(cls) -> sqlite3.Connection:
        if cls.__connection is None:
            cls.__connection = sqlite3.connect(DB_FILE_NAME)
            cls.__connection.row_factory = sqlite3.Row
            cls.__connection.set_trace_callback(cls.__sql_trace_callback)
        return cls.__connection

    @classmethod
    def __sql_trace_callback(cls, statement: str) -> None:
        print("[SQLite info]", statement)

    @classmethod
    def close_connection(cls) -> None:
        if cls.__connection is not None:
            cls.__connection.close()
            cls.__connection = None
