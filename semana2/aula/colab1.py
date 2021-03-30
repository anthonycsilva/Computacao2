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


listaClientes = [conta_gabriel, conta_leticia]

print(listaClientes[0].nome, listaClientes[0].cpf)