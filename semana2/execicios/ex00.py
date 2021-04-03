class Pilha():
    def __init__(self, lista):
        if type(lista) == list:
            self.lista = lista
            print(f'Lista Instanciada com Sucesso. {self.lista}')
        else:
            self.lista = list()
            print(f'Erro, O input não era uma lista. {self.lista}')
    
    def empilhar(self, elemento):
        self.lista.append(elemento)
        print(f'Elemento Empilhado: {elemento}. {self.lista}')
    
    def desempilhar(self):
        if len(self.lista) == 0:
            print('Erro, Lista Vazia!')
        else:
            elemento = self.lista.pop()
            print(f'Elemento Removido da Pilha: {elemento}. {self.lista}')

    
    def getPilha(self):
        print(self.lista)
    
    def lenPilha(self):
        print(len(self.lista))

    def __add__(self, elemento):
        resultado = self.lista + elemento.lista
        return resultado
    def __len__(self):
    #Professora, eu estava estudando sobre esses dunders, e queria testar esse do len. Por isso coloquei aqui
        return len(self.lista)

#Teste de execução

pilha1 = Pilha([1,7,9])
pilha2 = Pilha(3)
pilha2.empilhar(4)
pilha2.empilhar(10)
pilha2.getPilha()
pilha2.desempilhar()
pilha2.desempilhar()
pilha2.desempilhar()
pilha2.empilhar(5)
pilha3 = Pilha(pilha1+pilha2)
pilha3.lenPilha()
print(len(pilha3))
