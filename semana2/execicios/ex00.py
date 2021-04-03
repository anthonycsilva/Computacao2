#01: Fazer a classe Pilha, usar o método construtor (famoso _init_)

class Pilha:
    def __init__(self,elements = list()):
        if type(elements) == list:
            self.elements = elements.copy()
            print(f'Lista Instanciada: {self.elements}')
        else:
            self.elements = list()
            print(f'Erro, o elemento n era uma lista, mas agora é! : {self.elements}')

 #02: Criar o método Empilhar, colocando coisas na Pilha

    def empilhar(self, element):
        added = self.elements.append(element)
        print(f'Elemento Adicionado: {element}')
        return None

#03: Criar o método Desempilhar, retirando os elementos da Pilha

    def desempilhar(self):
        removed = self.elements.pop()
        print(f'Elemento Retirado: {removed}')
        return None

#04: Criar o método getPilha, para retornar os elementos da pilha

    def getPilha(self):
        print(f'{self.elements}')
        return self.elements


#05: Criar o método lenPilha, para saber o tamanho da pilha

    def getLen(self):
        print(f'Tamanho da Lista: {len(self.elements)}')
        
#06: Criar o método somaPilha, juntando duas pilhas em uma


    def __add__(self, lista):
        result = self.elements + lista.elements
        return result



pilha1 = Pilha([1,7,9])
pilha2 = Pilha([4,10])
pilha2.getPilha()
pilha2.desempilhar()
pilha2.getPilha()
pilha2.empilhar(5)
pilha2.getPilha()

pilha3 = Pilha(pilha2 + pilha1)
pilha4 = Pilha(pilha1 + pilha2)

pilha2.getLen()
