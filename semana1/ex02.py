import random
def criaCartela(quantidade, cartelas):
#Essa função cria a cartela, porém somente com numeros 0 em todas suas linhas e colunas
    i = 0
    while i < quantidade:
        cartelas.append([[0 for c in range(1,4)],[0 for l in range(1,4)],[0 for p in range(0,1)]])
        i+=1
    return cartelas


def adicionaNumero(cartelas):
#Essa função adiciona numeros aleatórios de 1 até 60 nas linhas e colunas da cartela
    for cartela in range(0,len(cartelas)):
        for coluna in range(0,2):
            for linha in range(0,3):
                cartelas[cartela][coluna][linha] = random.randint(1,61)
    return cartelas


def analisaCartela(cartelas):
#Essa função analisa se o numero da cartela atual, bate com um numero sorteado que vai de 1 até 60
    for cartela in range(0, len(cartelas)):
        for coluna in range(0,2):
            for linha in range(0,3):
                if cartelas[cartela][coluna][linha] == random.randint(1,61):
                    cartelas[cartela][2].append(1)
    return cartelas

def verificaSorteio():
#Função principal
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
#Todas as funções trabalham com a mesma variável porém a modificam conforme forem chamadas durante a execução
