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

    return pontuacao_maxima, local_sorteado, estado_sorteado, clima_sorteado, vitimas_sorteadas

def escolher_equipamentos(estado_vitima: str, clima: str) -> int:
    print("=== EQUIPAMENTOS ===")
    print("1 - LEO")
    print("2 - Drone")
    print("3 - Ambos")

    equipamentos = int(input("Escolha: "))
    pontos = 0

    match equipamentos:
        case 1:
            print("LEO utilizado com sucesso!")
            pontos = 20

        case 2:
            print("Drone Utilizado com sucesso!")
            pontos = 50
            if clima == "Tempestade":
                print("Tempestade! Drone perdeu sinal.")
                pontos -= 70

        case 3:
            print("Drone e LEO utilizados com sucesso!")
            pontos = 100
            if estado_vitima == "Fratura Leve":
                print("Uso excessivo de recursos!")
                pontos -= 150

        case _:
            pontos = 0

    print(f"Pontuação equipamentos: {pontos}")
    return pontos


def escolher_equipe(estado_vitima: str, quantidade_vitimas: int) -> int:
    print("=== EQUIPE ===")
    print("1 - UBS")
    print("2 - USA")

    equipe = int(input("Escolha: "))
    pontos = 0

    gravidade_real = estado_vitima
    if quantidade_vitimas == 3:
        gravidade_real = "Risco de Vida"

    match equipe:
        case 1:
            print("UBS selecionada")
            pontos = 50

            if gravidade_real == "Risco de Vida":
                print("Equipe insuficiente!")
                pontos -= 70

        case 2:
            print("USA selecionada")
            pontos = 100

            if gravidade_real == "Fratura Leve" and quantidade_vitimas == 1:
                print("Uso excessivo de equipe!")
                pontos -= 120

        case _:
            pontos = 0

    print(f"Pontuação equipe: {pontos}")
    return pontos


def forma_resgate(local: str, clima: str) -> int:
    print("=== RESGATE ===")
    print("1 - Aéreo")
    print("2 - Terrestre")
    print("3 - Marítimo")

    resgate = int(input("Escolha: "))
    pontos = 0

    match resgate:
        #SE O LOCAL FOR PRAIA
        case 3 if local == "Praia":
            print("Resgate marítimo enviado ao local.")
            pontos = 100

        case 2 if local == "Praia":
            print("Resgate terrestre enviado ao local.")
            pontos = 50

        case 1 if local == "Praia":
            print("Resgate aéreo enviado ao local.")
            pontos = -20

        #SE O LOCAL FOR FLORESTA
        case 2 if local == "Floresta":
            print("Resgate terrestre enviado ao local.")
            pontos = 100

        case 1 if local == "Floresta":
            print("Resgate aéreo enviado ao local.")
            pontos = 50

        case 3 if local == "Floresta":
            print("Resgate marítimo inválido!")
            pontos = -20

        #SE O LOCAL FOR MONTANHA
        case 1 if local == "Montanha":
            print("Resgate aéreo enviado ao local.")
            pontos = 100

        case 2 if local == "Montanha":
            print("Resgate terrestre enviado ao local.")
            pontos = 50

        case 3 if local == "Montanha":
            print("Resgate marítimo inválido!")
            pontos = -20

        case _:
            pontos = 0

    if clima == "Tempestade" and resgate == 1:
        print("Tempestade! Resgate aéreo comprometido!")
        pontos -= 50

    print(f"Pontuação resgate: {pontos}")
    return pontos


def pontuacao_final(maxima, equip, equipe, resgate):
    desempenho = (equip + equipe + resgate) / 3
    return maxima * (desempenho / 100)


def resultado(final, maxima):
    print("=== RESULTADO ===")
    print(f"Máxima: {maxima}")
    print(f"Final: {final:.1f}")

    perc = (final / maxima) * 100
    print(f"Desempenho: {perc:.1f}%")

    if perc >= 90:
        print("Excelente trabalho! Todas as vítimas foram salvas com máxima eficiência.")

    elif perc >= 70:
        print("Bom trabalho! O resgate foi realizado com poucos problemas.")

    elif perc >= 50:
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