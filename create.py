import json
from menus import tela_inicial
#tarefa tem que ter:
#- id
#- nome da tarefa 
#- status (Pendente, fazendo, feito)

def create_tarefa():
    
    while True:

        tarefa = []

        id = int(input("Digite a id da tarefa:"))
        tarefa.append(id)
        nome_tarefa = input("Digite o nome da tarefa:")
        tarefa.append(nome_tarefa)
        status = input("Digite o status da tarefa (Pendente, Fazendo ou Feito): ")
        tarefa.append(status)
        if status not in ["Pendente", "Fazendo", "Feito"]:
            print("Status inválido. Por favor, escolha entre 'Pendente', 'Fazendo' ou 'Feito'.")

        tarefa = {
            "id": id,
            "nome_tarefa": nome_tarefa,
            "status": status
        }

        with open("tarefa.json", "w") as arquivo:
            json.dump(tarefa, arquivo, indent=4)

        print("Você deseja criar um novo? (1) Sim (2) Não")
        escolha_create = int(input("Digite a opção: "))

        if escolha_create == 1:
            continue
        elif escolha_create == 2:
            print("Você saiu do menu de criação de tarefa.")
            tela_inicial()
            break
        else:
            print("Opção inválida. Por favor, escolha 1 ou 2.")
            return