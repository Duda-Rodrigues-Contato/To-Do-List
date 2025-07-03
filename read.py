import json


def read_tarefa():
    with open("tarefa.json", "r") as arquivo:
        tarefa = json.load(arquivo)
        print("\nDados da Tarefa:\n")
        print(f"ID: {tarefa['id']}")
        print(f"Nome da Tarefa: {tarefa['nome_tarefa']}")
        print(f"Status: {tarefa['status']}")
