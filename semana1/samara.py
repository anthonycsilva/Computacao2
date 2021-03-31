def artilheiros():
    #funcao que recebe e armazena o nome, a rodada e os gols que um jogador fez na Copa em uma matriz
    #none -> list(list)
    return none

def inserirJogador(matrizJogadores):
    nome = str(input("Insira o nome do jogador: "))
    print("[3] - classificatorias",end="\n")
    print("[4] - oitavas", end="\n")
    print("[5] - quartas", end="\n")
    print("[6] - semi", end="\n")
    print("[7] - final", end="\n")

    rodada = int(input("Insira o número correspondente da rodada que o jogador atuou: "))
    gol = int(input("Insira o número de gols realizados pelo jogador: "))

    matrizInformacao = [nome,rodada,gol]
    matrizJogadores.append(matrizInformacao)
    print(f'Tabela de jogadores: {matrizJogadores}')
    return matrizJogadores

def mediaGols(matrizJogadores):
    #funcao que calcula a media de gols dos jogadores na Copa, media feita pela razao do numero de gols feito e numero de partidas jogadas
    #list(list) -> float

    for i in range(len(matrizJogadores)):

        media = round((matrizJogadores[i][2]/matrizJogadores[i][1]),2)
        matrizJogadores[i].append(media)

    return matrizJogadores



def chuteiraOuro():
    matrizJogadores = list()
    matrizJogadores = inserirJogador(matrizJogadores)
    while True:
        opc = int(input('Deseja Adicionar mais jogadores:? 1 - sim, 2 - nao: '))
        if opc == 1:
            inserirJogador(matrizJogadores)
            continue
        elif opc == 2:
            break
    mediaGols(matrizJogadores)

    if(len(matrizJogadores) == 1):
        print(f'Parabens, vc {matrizJogadores[0][0]} só ganhou pq estava jogando contra ninguém, media: {matrizJogadores[0][3]}')
        return matrizJogadores
    
    else:
        ganhador = list()

        for jogadores in range(0, len(matrizJogadores)):
            if len(ganhador) == 0:
                ganhador = matrizJogadores
            else:
                if matrizJogadores[jogadores][3] >= ganhador[0][3]:
                    ganhador[0] = matrizJogadores[jogadores]                
    return ganhador[0]
            



print(chuteiraOuro())