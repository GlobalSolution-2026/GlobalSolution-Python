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

    if pontuacao_maxima > 300:
        pontuacao_maxima = 300

    print("Analisando a situação ...")
    print(f"Clima: {clima_sorteado}")
    print(f"Vítimas: Quantidade de vítimas: {vitimas_sorteadas}, Estado da vítima: {estado_sorteado}")
    print(f"Localização: {local_sorteado}")
    print(f"Pontuação máxima possível: {pontuacao_maxima}")

    return pontuacao_maxima, local_sorteado, estado_sorteado, clima_sorteado, vitimas_sorteadas

def escolher_equipamentos(estado_vitima: str, clima: str, vitimas_sorteadas: int) -> int:
    print("=== EQUIPAMENTOS ===")
    print("1 - LEO")
    print("2 - Drone")
    print("3 - Ambos")

    while True:
        equipamentos = input("Escolha: ").strip()
        if not equipamentos.isdigit():
            print("Digite apenas números.")
            continue
        equipamentos = int(equipamentos)
        break

    pontos = 0

    match equipamentos:
        case 1:
            if vitimas_sorteadas > 1: 
                print(f"LEO Utilizado com sucesso! As {vitimas_sorteadas} vítimas com {estado_vitima} possuem sinal para comunicação")
            else:
                print(f"LEO Utilizado com sucesso! A {vitimas_sorteadas} vítima com {estado_vitima} possui sinal para comunicação")

            if clima == "Tempestade":
                pontos = 100
            else:
                pontos = 40

        case 2:
            if vitimas_sorteadas > 1: 
                print(f"Drone Utilizado com sucesso! Foram localizadas as {vitimas_sorteadas} vítimas com {estado_vitima}")
            else:
                print(f"Drone Utilizado com sucesso! Foi localizada {vitimas_sorteadas} vítima com {estado_vitima}")

            if clima == "Tempestade":
                print("Tempestade! Drone prejudicado.")
                pontos = -30

            else:
                if estado_vitima == "Fratura Leve" and quantidade_vitimas == 1:
                    pontos = 100
                else:
                    pontos = 80

        case 3:
            if vitimas_sorteadas > 1: 
                print(f"Drone e LEO Utilizados com sucesso! Foram localizadas as {vitimas_sorteadas} vítimas com {estado_vitima} e agora elas possuem sinal para comunicação")
            else:
                print(f"Drone e LEO Utilizados com sucesso! Foi localizada {vitimas_sorteadas} vítima com {estado_vitima} e agora ela possui sinal para comunicação")

            if estado_vitima == "Fratura Leve" and quantidade_vitimas == 1:
                pontos = -30
            else:
                pontos = 100

        case _:
            pontos = 0

    print(f"Pontuação equipamentos: {pontos}")
    return pontos

def escolher_equipe(estado_vitima: str, quantidade_vitimas: int) -> int:
    print("=== EQUIPE ===")
    print("1 - UBS (Unidade Básica de Saúde)")
    print("2 - USA (Unidade Avançada de Saúde)")

    while True:
        equipe = input("Escolha: ").strip()
        if not equipe.isdigit():
            print("Digite apenas números.")
            continue
        equipe = int(equipe)
        break
    
    pontos = 0

    if quantidade_vitimas == 3:
        gravidade_real = "Risco de Vida"
    else:
        gravidade_real = estado_vitima

    match equipe:
        case 1:
            print("UBS selecionada")

            if gravidade_real == "Fratura Leve":
                pontos = 100  
            elif gravidade_real == "Fratura Exposta":
                pontos = 50
            else:
                print("Equipe insuficiente!")
                pontos = -20  

        case 2:
            print("USA selecionada")

            if gravidade_real == "Risco de Vida":
                pontos = 100  
            elif gravidade_real == "Fratura Exposta":
                pontos = 70
            else:
                print("Uso excessivo de equipe!")
                pontos = -20  

        case _:
            pontos = 0

    print(f"Pontuação equipe: {pontos}")
    return pontos


def forma_resgate(local: str, clima: str) -> int:
    print("=== RESGATE ===")
    print("1 - Aéreo")
    print("2 - Terrestre")
    print("3 - Marítimo")

    while True:
        resgate = input("Escolha: ").strip()
        if not resgate.isdigit():
            print("Digite apenas números.")
            continue
        resgate = int(resgate)
        break

    pontos = 0
    
    #LOCAL
    if local == "Praia":
        melhor = 3 if clima != "Tempestade" else 2

    elif local == "Floresta":
        melhor = 2

    elif local == "Montanha":
        melhor = 1 if clima != "Tempestade" else 2

    #PONTUACAO
    if resgate == melhor:
        pontos = 100
    elif resgate in [1, 2, 3]:
        pontos = 50
    else:
        pontos = 0

    #PENALIDADES
    if resgate == 3 and (local == "Floresta" or local == "Montanha"):
        print("Resgate marítimo inválido!")
        pontos -= 20
    if clima == "Tempestade" and resgate == 1:
        print("Tempestade! Resgate aéreo comprometido!")
        pontos -= 50

    #MENSAGENS
    if resgate == 1:
        print("Resgate aéreo enviado ao local.")
    elif resgate == 2:
        print("Resgate terrestre enviado ao local.")
    elif resgate == 3 and local == "Praia":
        print("Resgate marítimo enviado ao local.")

    print(f"Pontuação resgate: {pontos}")
    return pontos


def pontuacao_final(maxima: int, equip: int, equipe: int, resgate: int) ->float:
    desempenho = (equip + equipe + resgate) / 3
    return maxima * (desempenho / 100)


def resultado(final: float, maxima: int) ->float:
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
       O projeto propõe o uso de Análise Preditiva e o Processo de Decisão de Markov (MDP) para otimizar operações de resgate em cenários críticos. Tecnologias garantem comunicação e coleta de dados mesmo em regiões sem conexão, alimentando o algoritmo em tempo real. Como prova de conceito, foi desenvolvido um modelo simplificado que simula decisões considerando 5 variáveis: condição da vítima, tempo de resgate, localização, meteorologia e equipe disponível.
        """)