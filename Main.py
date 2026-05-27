from functions import *

clear_screen()

logged_in = False

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
            pontuacao_maxima, local_sorteado = avaliar_situacao()

        case 2:
            pontos_equipamentos = escolher_equipamentos()

        case 3:
            if local_sorteado != "":
                pontos_resgate = forma_resgate(local_sorteado)

            else:
                print("Avalie a situação primeiro.")

        case 4:
            pontos_equipe = escolher_equipe()

        case 5:
            pontuacao_final = pontuacao(pontuacao_maxima, pontos_equipamentos, pontos_equipe, pontos_resgate)
            finalizar_cenario(pontuacao_final, pontuacao_maxima)

        case 6:
            print("Encerrando ...")
            break

        case _:
            print("Apenas opções de 1 a 6.")
    input("Pressione Enter para continuar... ")