from controllers import *

def menu():
    while True:
        print("\n1 - Criar usuário")
        print("2 - Listar usuários")
        print("3 - Criar tarefa")
        print("4 - Listar tarefas")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            create_user(nome, email)

        elif escolha == "2":
            usuarios = list_users()
            if usuarios != []:
                for u in usuarios:
                    print(f"ID: {u[0]}, Nome: {u[1]}, Email: {u[2]}")
            else:
                print("Não existem usuarios para serem listados")

        elif escolha == "3":
            nome = input("Nome da tarefa: ")
            descricao = input("Descrição: ")
            status = input("Status (pendente/em andamento/concluido): ")
            usuario = int(input("ID do usuário: "))
            create_task(nome, descricao, status, usuario)

        elif escolha == "4":
            tarefas = list_tasks()
            if tarefas != []:
                for t in tarefas:
                    print(f"ID: {t[0]}, Nome: {t[1]}, Descrição: {t[2]}, Status: {t[3]}, Usuário ID: {t[4]}")
            else:
                print("Não existem tarefas para serem listados")

        elif escolha == "0":
            break

        else:
            print("Opção inválida! Tente novamente.")