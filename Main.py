from functions import *

clear_screen()

logged_in = False
pontuacao_maxima = 0
local_sorteado = ""
estado = ""
clima = ""
vitimas = 0
pontos_equipamentos = 0
pontos_resgate = 0
pontos_equipe = 0


print("Bem-Vindo ao Firefly Rescue")

while True:
    print("""
      1- Sobre o Projeto
      2- Cadastrar Socorrista
      3- Acessar Menu Principal
      """)
    opcao = int(input("Selecione uma opção de 1 a 3: "))
    match opcao:
        case 1:
            sobre_projeto()
        case 2:
            name = input("Nome: ")
            while len(name) < 3:
                print("Nome precisa ter pelo menos 3 letras.")
                name = input("Nome: ")
            rm = input("Rm: ")
            while len(rm) != 6:
                print("RM precisa ter 6 dígitos.")    
                rm = input("RM: ")
            logged_in = cadastro_socorrista(name, rm)
        case 3:
            if logged_in == True:
                print("Acessando Menu Principal ...")
                break
            else:
                print("Se cadastre como socorrista primeiro.")
        case _:
            print("Apenas de 1 a 3.")
    input("Pressione Enter para continuar... ")

while True:
    print(("-" * 20) + " Menu Principal " + ("-" * 20))
    print("""
          1-Avaliar Situação
          2-Escolher Equipamentos
          3-Forma de Regaste
          4-Selecionar Equipe
          5-Finalizar Cenário
          6-Sair
          """)
    print("-" * 50)
    opcao = int(input("Selecione uma opção de 1 a 6: "))

    match opcao:

        case 1:
            pontuacao_maxima, local_sorteado, estado, clima, vitimas = avaliar_situacao()

        case 2:
            if estado != "" and clima != "":
                pontos_equipamentos = escolher_equipamentos(estado, clima)
            else:
                print("Avalie a situação primeiro.")

        case 3:
            if local_sorteado != "" and clima != "":
                pontos_resgate = forma_resgate(local_sorteado, clima)
            else:
                print("Avalie a situação primeiro.")

        case 4:
            if estado != "" and vitimas != 0:
                pontos_equipe = escolher_equipe(estado, vitimas)
            else:
                print("Avalie a situação primeiro.")

        case 5:
            if pontuacao_maxima != 0:
                pont_final = pontuacao_final(pontuacao_maxima, pontos_equipamentos, pontos_equipe, pontos_resgate)
                resultado(pont_final, pontuacao_maxima)
            else:
                print("Complete pelo menos a avaliação primeiro.")

        case 6:
            print("Encerrando...")
            break

        case _:
            print("Apenas opções de 1 a 6.")
    input("Pressione Enter para continuar...")