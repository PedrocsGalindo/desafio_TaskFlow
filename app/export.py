import json

arquivo = "tasks.json"

# Sera sobrescrito caso ja haja valor

def export_task(tarefa):
    with open(arquivo, mode='w', encoding='utf-8') as arquivo_json:
        json.dump(tarefa, arquivo_json, indent=4, ensure_ascii=False)

def export_tasks(tarefas):
    with open(arquivo, mode='w', encoding='utf-8') as arquivo_json:
        json.dump(tarefas, arquivo_json, indent=4, ensure_ascii=False)