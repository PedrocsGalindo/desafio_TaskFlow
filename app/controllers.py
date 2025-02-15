from config import connect

# criar usuario
def create_user(name, email):
    connection, cursor = connect()
    try:
        cursor.execute("INSERT INTO usuario (nome, email) VALUES (?, ?)", (name, email))
        connection.commit()
        print("Cadastro com sucesso!")
    except Exception as e:
        print("Erro ao cadastrar usuário:", e)
    finally:
        connection.close()

# retorna uma lista de tuplas, com os atributos do usuario (id, nome, email)
def list_users():
    connection, cursor = connect()
    cursor.execute("SELECT * FROM usuario")
    usuarios = cursor.fetchall()
    connection.close()
    return usuarios

# criar tarefa
def create_task(tittle, description, status, user):
    connection, cursor = connect()
    try:

        # Verificação da existencia do usuario
        cursor.execute("SELECT id FROM usuario WHERE id = ?", (user))
        user = cursor.fetchone()
        if user is None:  
            print(f"Erro: Usuário com ID {user} não encontrado.")
            return
        
        # Caso o usuario exista, cria
        cursor.execute("INSERT INTO tarefa (titulo, descricao, status, usuario) VALUES (?, ?)", (tittle, description, status, user))
        connection.commit()
        print("Cadastro com sucesso!")
    except Exception as e:
        print("Erro ao cadastrar usuário:", e)
    finally:
        connection.close()

# retorna uma lista de tuplas, com os atributos da tarefa (titulo, descricao, status, usuario)
def list_tasks():
    connection, cursor = connect()
    cursor.execute("SELECT * FROM tarefa")
    tarefas = cursor.fetchall()
    connection.close()
    return tarefas

# retorna a tarefa
def get_task_by_id(id):
    connection, cursor = connect()
    cursor.execute("SELECT id FROM tarefa WHERE id = ?", (id))
    tarefa = cursor.fetchone()
    return tarefa
    


