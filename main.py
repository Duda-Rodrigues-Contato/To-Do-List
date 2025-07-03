import json
from menus import *
from create import *
from read import *

tela_inicial()

opcao = int(input("Digite a escolha: "))

match opcao:
    case 1:
        create_tarefa()
    case 2:
        read_tarefa()
    case _:
        print("Opção inválida. Tente novamente.")