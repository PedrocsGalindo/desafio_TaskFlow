from controllers import *
from export import *

dict_status = {1:'pendente', 2:'em andamento', 3:'concluido'}

def menu():
    while True:
        print("\n1 - Criar usuário")
        print("2 - Listar usuários")
        print("3 - Criar tarefa")
        print("4 - Listar tarefas")
        print("5 - Exportar tarefas")
        print("4 - Exportar tarefa")
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
            while True:
                try:
                    status = int(input("Status \n1 - pendente\n2 - em andamento\n3- concluido\n"))
                    if status in dict_status:
                        status = dict_status[status]
                        break
                    else:
                        print("Opção inválida! Tente novamente.")
                except ValueError:
                    print("Erro: Digite um número válido (1, 2 ou 3).")
            usuario = int(input("ID do usuário: "))
            create_task(nome, descricao, status, usuario)

        elif escolha == "4":
            tarefas = list_tasks()
            if tarefas != []:
                for t in tarefas:
                    print(f"ID: {t[0]}, Nome: {t[1]}, Descrição: {t[2]}, Status: {t[3]}, Usuário ID: {t[4]}")
            else:
                print("Não existem tarefas para serem listados")

        elif escolha == "5":
            tarefas = list_tasks()
            if tarefas == []:
                print("Não existem tarefas para serem listadas")
            else:
                export_tasks(tarefas)

        elif escolha == "6":
            try:   
                tarefa = int(input("ID da tarefa: "))
                tarefa = get_task_by_id(tarefa)
                if tarefa == None:
                    print("Tarefa não econtrada")
                else:
                    export_task(tarefa)
            except ValueError:
                print('Escreva um valor numerico')

        elif escolha == "0":
            break

        else:
            print("Opção inválida! Tente novamente.")