from common.repository.base_repository import Connection


def create_if_not_exists():
    conn = Connection.get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
CREATE TABLE IF NOT EXISTS cidade (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
        """
    )

    cursor.execute(
        """
CREATE TABLE IF NOT EXISTS cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT,
    cidade_id INTEGER NOT NULL,
    FOREIGN KEY(cidade_id) REFERENCES cidade(id) ON DELETE RESTRICT
)
        """
    )

    cursor.execute(
        """
CREATE TABLE IF NOT EXISTS produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    unidade_medida TEXT NOT NULL
)
        """
    )

    cursor.execute(
        """
CREATE TABLE IF NOT EXISTS pedido (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_hora TEXT NOT NULL,
    status TEXT NOT NULL,
    cliente_id INTEGER NOT NULL,
    FOREIGN KEY(cliente_id) REFERENCES cliente(id) ON DELETE RESTRICT
)
        """
    )

    cursor.execute(
        """
CREATE TABLE IF NOT EXISTS pedido_produto (
    pedido_id INTEGER,
    produto_id INTEGER,
    quantidade INTEGER NOT NULL,
    FOREIGN KEY(pedido_id) REFERENCES pedido(id) ON DELETE CASCADE,
    FOREIGN KEY(produto_id) REFERENCES produto(id) ON DELETE CASCADE,
    PRIMARY KEY (pedido_id, produto_id)
)
        """
    )

    conn.commit()
    cursor.close()
    Connection.close_connection()
