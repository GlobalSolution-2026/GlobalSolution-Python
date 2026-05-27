import random
def clear_screen() ->None:
    import os
    os.system("cls" if os.name == "nt" else "clear")

clima = ["Limpo", "Neblina", "Tempestade"]
localizacao = ["Praia", "Floresta", "Montanha"]
estado_vitima = ["Fratura Leve", "Fratura Exposta", "Risco de Vida"]
quantidade_vitimas = [1, 2, 3]


def cadastro_socorrista(name: str,rm: str) ->bool:
    print(f"RM-{rm}: {name}")
    print(f"Olá {name}, você é um socorrista que foi chamado para um cenário de resgate, seu objetivo é realizar o resgate alcançando a pontuação máxima e salvando as vítimas da melhor forma possível. Boa Sorte")
    return True

def avaliar_situacao() ->tuple[int, str]:
    clima_sorteado = random.choice(clima)
    local_sorteado = random.choice(localizacao)
    estado_sorteado = random.choice(estado_vitima)
    vitimas_sorteadas = random.choice(quantidade_vitimas)

    pontuacao_maxima = 0

    match vitimas_sorteadas:
        case 1:
            pontuacao_maxima += 20
        case 2:
            pontuacao_maxima += 50
        case 3:
            pontuacao_maxima += 100

    match estado_sorteado:
        case "Fratura Leve":
            pontuacao_maxima += 20
        case "Fratura Exposta":
            pontuacao_maxima += 50
        case "Risco de Vida":
            pontuacao_maxima += 100

    match clima_sorteado:
        case "Limpo":
            pontuacao_maxima += 20
        case "Neblina":
            pontuacao_maxima += 50
        case "Tempestade":
            pontuacao_maxima += 100

    match local_sorteado:
        case "Praia":
            pontuacao_maxima += 20
        case "Floresta":
            pontuacao_maxima += 50
        case "Montanha":
            pontuacao_maxima += 100

    print("Analisando a situação ...")
    print(f"Clima: {clima_sorteado}")
    print(f"Vítimas: Quantidade de vítimas: {vitimas_sorteadas}, Estado da vítima: {estado_sorteado}")
    print(f"Localização: {local_sorteado}")
    print(f"Pontuação máxima possível: {pontuacao_maxima}")

    return pontuacao_maxima, local_sorteado

def escolher_equipamentos() -> int:

    print("\n=== ESCOLHA DOS EQUIPAMENTOS ===")
    print("1 - LEO (Low Earth Orbital)")
    print("2 - Drone sem LEO")
    print("3 - Ambos")

    equipamento = int(input("Escolha uma opção: "))

    match equipamento:

        case 1:
            print("Você escolheu utilizar apenas o LEO.")
            print("Menor precisão no resgate.")
            pontuacao_equipamentos = 20

        case 2:
            print("Você escolheu utilizar Drone sem LEO.")
            print("Precisão intermediária no resgate.")
            pontuacao_equipamentos = 50

        case 3:
            print("Você escolheu utilizar ambos os equipamentos.")
            print("Máxima eficiência no resgate.")
            pontuacao_equipamentos = 100

        case _:
            print("\nOpção inválida.")
            pontuacao_equipamentos = 0

    print(f"Pontuação obtida pelos equipamentos: {pontuacao_equipamentos}")

    return pontuacao_equipamentos

def escolher_equipe() -> int:

    print("=== ESCOLHA DA EQUIPE ===")
    print("1 - UBS")
    print("2 - USA")

    equipe = int(input("Escolha uma equipe: "))

    match equipe:

        case 1:
            print("Equipe UBS selecionada.")
            print("Atendimento básico.")
            pontuacao_equipe = 50
            equipe_escolhida = "UBS"

        case 2:
            print("Equipe USA selecionada.")
            print("Atendimento avançado.")
            pontuacao_equipe = 100
            equipe_escolhida = "USA"

        case _:
            print("Opção inválida.")
            pontuacao_equipe = 0
            equipe_escolhida = "Nenhuma"

    print(f"Equipe escolhida: {equipe_escolhida}")
    print(f"Pontuação da equipe: {pontuacao_equipe}")

    return pontuacao_equipe


def forma_resgate(localizacao_sorteada: str) -> int:

    print("=== FORMA DE RESGATE ===")
    print("1 - Aérea")
    print("2 - Terrestre")
    print("3 - Marítima")

    opcao = int(input("Escolha a forma de resgate: "))

    pontuacao_resgate = 0

    match opcao:

        # PRAIA
        case 3 if localizacao_sorteada == "Praia":
            print("Resgate marítimo foi a melhor escolha.")
            pontuacao_resgate = 100

        case 2 if localizacao_sorteada == "Praia":
            print("\nResgate terrestre foi razoável.")
            pontuacao_resgate = 50

        case 1 if localizacao_sorteada == "Praia":
            print("Resgate aéreo não foi a melhor escolha.")
            pontuacao_resgate = 20

        # FLORESTA
        case 2 if localizacao_sorteada == "Floresta":
            print("Resgate terrestre foi a melhor escolha.")
            pontuacao_resgate = 100

        case 1 if localizacao_sorteada == "Floresta":
            print("Resgate aéreo foi razoável.")
            pontuacao_resgate = 50

        case 3 if localizacao_sorteada == "Floresta":
            print("Resgate marítimo não faz sentido nesse local.")
            pontuacao_resgate = 20

        # MONTANHA
        case 1 if localizacao_sorteada == "Montanha":
            print("Resgate aéreo foi a melhor escolha.")
            pontuacao_resgate = 100

        case 2 if localizacao_sorteada == "Montanha":
            print("Resgate terrestre foi razoável.")
            pontuacao_resgate = 50

        case 3 if localizacao_sorteada == "Montanha":
            print("Resgate marítimo não foi adequado.")
            pontuacao_resgate = 20

        case _:
            print("Opção inválida.")
            pontuacao_resgate = 0

    print(f"Pontuação da forma de resgate: {pontuacao_resgate}")

    return pontuacao_resgate


def pontuacao(pontuacao_maxima: int, pontuacao_equipamentos: int, pontuacao_equipe: int, pontuacao_resgate: int) -> float:
    desempenho = (pontuacao_equipamentos + pontuacao_equipe + pontuacao_resgate) / 3
    pontuacao_final = pontuacao_maxima * (desempenho / 100)
    return pontuacao_final


def finalizar_cenario(pontuacao_final: float, pontuacao_maxima: int) -> None:

    print("=== RESULTADO FINAL ===")

    print(f"Pontuação máxima: {pontuacao_maxima}")

    print(f"Pontuação obtida: {pontuacao_final:.1f}")

    porcentagem = (pontuacao_final / pontuacao_maxima) * 100

    print(f"Desempenho: {porcentagem:.1f}%")

    if porcentagem >= 90:
        print("Excelente trabalho! Todas as vítimas foram salvas com máxima eficiência.")

    elif porcentagem >= 70:
        print("Bom trabalho! O resgate foi realizado com poucos problemas.")

    elif porcentagem >= 50:
        print("Resgate concluído, mas houve dificuldades durante a operação.")

    else:
        print("O resgate falhou. Muitas decisões poderiam ter sido melhores.")

def sobre_projeto() ->None:
    print("""
        Uso de IA + Satélite para entendimento da melhor forma de acontecer um resgate, dentro dos problemas da região e fatores meteorológicas
            Uso de LEO para essas regiões sem conexão
            Usar o Processo de Decisão de Markov para entendimento de como vai acontecer a situação
        Como PDK uso uma matemática bem difícil e processamento de dados que ainda não vimos. Achamos um jeito simplificado de usar. Ele dependeria do tempo, equipe, vítimas, clima e região. 
          """)