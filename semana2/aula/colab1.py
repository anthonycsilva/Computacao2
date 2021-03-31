class Conta:
    def __init__(self, nome, cpf, saldo = 0):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo

    def mostra(self):
        print(f'Nome: {self.nome}, Saldo:{self.saldo}')

    def saque(self, valor):
        if self.saldo <= valor:
            print('insuficiente')
        else:
            self.saldo -= valor
            print('Operação concluida')
    def deposito(self, valor):
        self.saldo += valor
        print('Deposito concluido')


conta_leticia = Conta('Leticia', '111.111.111-00')
conta_gabriel = Conta('Gabriel','111.111.111-01')




import random

class Aluno:
    def __init__(self, nome, id, nota1=0,nota2=0):
        self.nome = nome
        self.id = random.randint(1,100)
        self.nota1 = nota1
        self.nota2= nota2

    def mostraNota(self):
        print(f'O Aluno, {self.nome}, Possui a média: {(self.nota1+self.nota2)/2}, id = {self.id}')


anthony = Aluno('Anthony',92832)

anthony.mostraNota()