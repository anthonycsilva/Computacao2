#PRIMEIRO PEPINO: DA UM JEITO DE ACHAR O MELHOR JOGADOR DA COPA
#CADA ARTILHEIO VAI RECEBER UMA ESPAÇO NA MATRIZ COM O NOME DELE, RODADA, NUMERO DE GOLS.
#SÓ QUE EM RODADA VAI ATÉ EM QUAL RODADA ELE JOGOU POR ULTIMO PODENDO SER, CLASSIFICATÓRIA, OITAVAS, QUARTAS, SEMI, FINAL

#QUEM JOGOU CLASSIFICATÓRIA JOGOU 3 JOGOS, OITAVAS 4, QUARTAS 5, SEMI 6, FINAL 7


#SEGUNDO PEPINO:FUNÇÕES MEDIAGOLS
#UMA FUNÇÃO QUE DADA A MATRIZ DE ARTILHEIROS, CALCULA A MATRIZ COM A MÉDIA DE GOLS DURANTE A COPA

#TERCEIRO PEPINO:FUNÇÃO CHUTEIRA DE OURO É SUA MAIN, AONDE AS OUTRAS DEVEM SER CHAMADAS, DEVE RETORNAR O JOGADOR COM A MAIOR MÉDIA DO CAMP E QUE TENHA IDO ALEM DAS CLASSIFICATÓRIAS, RETORNAR O NOME E A MÉDIA DE GOLS


def artilheiros():
    jogadores = [
                ['Anthony Perna Mansa',5,18],
                ['Samarinha Pé elétrico',6,10],
                ['Diego Beionce',4,12],
                ['Voldollar',7,14],
                ['Shrek Ninja',3,32],
                ]

    return jogadores

def mediaGolsJogadores(matrizJogadores):
    gols = list()
    classificados = list()
    for jogadores in range(0, len(matrizJogadores)):
        if matrizJogadores[jogadores][1] > 3:
            gols.append(matrizJogadores[jogadores][2])
            classificados.append(matrizJogadores[jogadores])
    return [(sum(gols)/len(matrizJogadores)), classificados]


def chuteiraOuro():
    dados = mediaGolsJogadores(artilheiros())
    media = dados[0]
    o_mais_pika = list()
    for jogadores in range(0, len(dados[1])):
        if len(o_mais_pika) == 0:
            o_mais_pika.append(dados[1][jogadores])
        else:
            if dados[1][jogadores][2] >= o_mais_pika[0][2]:
                o_mais_pika[0] = dados[1][jogadores]
    mediaGols = o_mais_pika[0][2]/o_mais_pika[0][1]
    print(f'O jogador, {o_mais_pika[0][0]}, recebeu a Chuteira de Ouro com uma Média de {mediaGols} gols por partida!')
    return True


chuteiraOuro()
