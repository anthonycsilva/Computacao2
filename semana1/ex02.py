#PRIMEIRO PEPINO, CRIAR UMA MATRIZ COM AS TABLEAS PARA O BINGO
#NUMEROS RANDOMS DE 1 A 60, SENDO QUE VOU FAZER ELAS DISTRIBUIDAS 2 X 3 ( 2 LINHAS PARA 3 COLUNAS )
import random
##[0 for linha in range(1,4)],[0 for coluna in range(1,4)]
cartelas = list()
def criaCartela(quantidade):
    i = 0
    while i < quantidade:
        cartelas.append([[0 for c in range(1,4)],[0 for l in range(1,4)]])
        i+=1
    return True


def adicionaNumero(cartelas):
    for cartela in range(0,len(cartelas)):
        for coluna in range(0,2):
            for linha in range(0,3):
                cartelas[cartela][coluna][linha] = random.randint(1,61)


def sorteiaNumero():
    numeroSorteado = random.randint(1,61)
    return numeroSorteado


def verificaSorteio(cartelas):
    
    while True:
        numero = sorteiaNumero()
        for cartela in range(0,len(cartelas)):
            for coluna in range(0,2):
                for linha in range(0,3):
                    if cartelas[cartela][coluna][linha] == numero:
                        print(cartelas[cartela])
                        print(numero)
                        return cartela+1
                    else: 
                        print('achei não mano')
    
    

                        
                     
criaCartela(5)
adicionaNumero(cartelas)
print(verificaSorteio(cartelas))