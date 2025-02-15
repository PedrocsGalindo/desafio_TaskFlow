import sqlite3

def connect():
    connection = sqlite3.connect("db_TaskFlow.db")
    cursor = connection.cursor()
    return connection, cursor

def create_tables():
    connection, cursor = connect()

    # tabela usuario
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)

    # tabela tarefa
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT NOT NULL,
            status TEXT CHECK(status IN ('pendente', 'em andamento', 'concluido')) NOT NULL,
            usuario INTEGER NOT NULL,
            FOREIGN KEY (usuario) REFERENCES usuario(id) ON DELETE CASCADE
        )
    """)

    connection.commit()  # Salva as alterações no banco
    connection.close()   # Fecha a conexão