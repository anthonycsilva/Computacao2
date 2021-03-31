def artilheiros():
    #Função que cria e instancia a matriz de jogadores
    matrizJogadores = [
                ['Anthony Perna Mansa',5,18],
                ['Samarainha',6,10],
                ['Diego Beionce',4,12],
                ['Voldollar',7,14],
                ['Shrek Ninja',3,32],
                ]

    return matrizJogadores


def mediaGols(matrizJogadores):
#função que tira a média de gols dos jogadores por partida
    for jogador in range(len(matrizJogadores)):
        media = (matrizJogadores[jogador][2]/matrizJogadores[jogador][1])
        media = round(media, 2)
        matrizJogadores[jogador].append(media)
    return matrizJogadores


def chuteiraOuro():
#função principal para deduzir qual foi o melhor jogar com base na sua média de gols por partida, porém somente se o jogador saiu das classificatórias 
    matrizJogadores = artilheiros()
    mediaGols(matrizJogadores)

    ganhador = list()

    for jogadores in range(0, len(matrizJogadores)):
        if matrizJogadores[jogadores][1] <4:
            del(matrizJogadores[jogadores])
        else: 
            if len(ganhador) == 0:
                ganhador = matrizJogadores
            else:
                if matrizJogadores[jogadores][3] >= ganhador[0][3]:
                    ganhador[0] = matrizJogadores[jogadores]
    print(f'O Jogador: {ganhador[0][0]}, ganhou o premio chuteira de ouro com uma média de: {ganhador[0][3]} gols por partida')                
    return ganhador[0]
chuteiraOuro()
