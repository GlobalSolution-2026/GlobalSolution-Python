from functions import *

clear_screen()

print("Bem-Vindo ao Firefly Rescue")

while True:
    print("""
          1-Cadastrar Socorrista
          2-Avaliar Situação
          3-Escolher Equipamentos
          4-Forma de Regaste
          5-Selecionar Equipe
          6-Finalizar Cenário
          7-Sobre o Projeto
          8-Sair
          """)
    opcao = int(input("Selecione uma opção de 1 a 8: "))
    match opcao:
        case 1:
            nome = input("Nome: ")
            rm = input("RM: ")
            cadastro_socorrista(nome, rm)
        case 2:
            avaliar_situacao()
        case 3:
            ...
        case 4:
            ...
        case 5:
            ...
        case 6:
            ...
        case 7:
            sobre_projeto()
        case 8:
            print("Encerrando ...")
            break
        case _:
            print("Apenas de 1 a 8.")
    input("Pressione Enter para continuar... ")