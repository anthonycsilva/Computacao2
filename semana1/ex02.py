#PRIMEIRO PEPINO, CRIAR UMA MATRIZ COM AS TABLEAS PARA O BINGO
#NUMEROS RANDOMS DE 1 A 60, SENDO QUE VOU FAZER ELAS DISTRIBUIDAS 2 X 3 ( 2 LINHAS PARA 3 COLUNAS )
import random
##[0 for linha in range(1,4)],[0 for coluna in range(1,4)]
def criaCartela(quantidade, cartelas):
    i = 0
    while i < quantidade:
        cartelas.append([[0 for c in range(1,4)],[0 for l in range(1,4)],[0 for p in range(0,1)]])
        i+=1
    return cartelas


def adicionaNumero(cartelas):
    for cartela in range(0,len(cartelas)):
        for coluna in range(0,2):
            for linha in range(0,3):
                cartelas[cartela][coluna][linha] = random.randint(1,61)
    return cartelas


def analisaCartela(cartelas):
    for cartela in range(0, len(cartelas)):
        for coluna in range(0,2):
            for linha in range(0,3):
                if cartelas[cartela][coluna][linha] == random.randint(1,61):
                    cartelas[cartela][2].append(1)
    return cartelas

def verificaSorteio():
    cartelas = list()
    cartelas = criaCartela(5, cartelas)
    cartelas = adicionaNumero(cartelas)
    ganhadora = list()
    numero = int()
    while True:
        cartelas = analisaCartela(cartelas)
        for cartela in range(0, len(cartelas)):
            if len(cartelas[cartela][2]) == 7:
                ganhadora.append(cartelas[cartela])
                numero = cartela
        if len(ganhadora) != 0:
            break
    print(f'Temos um ganhador! A Cartela Número: {numero+1}')
    print(f'Linha:  {ganhadora[0][0]}')
    print(f'Coluna: {ganhadora[0][1]}')
    return None

                        

verificaSorteio()

#adicionaNumero(cartelas)
#print(verificaSorteio(cartelas))
