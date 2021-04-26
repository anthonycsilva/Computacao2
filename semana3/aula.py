import random

class Client():
    def __init__(self, nome_do_cliente, cpf_do_cliente):
      self.nome = nome_do_cliente
      self.cpf = cpf_do_cliente

class ContaBancaria():
  def __init__(self, titulares, saldo_conta = 0,numero_conta = 0):
    self.saldo = saldo_conta
    self.numero_conta = random.randint(0, 1000)
    self.titulares = titulares
    self.operacoes = list()
    print(f'Conta Aberta, Numero: {self.numero_conta}')
    self.operacoes.append(['Saldo Inicial',0,self.saldo])

  def resumo_conta(self):
    print(f'Conta Corrente Número: {self.numero_conta}')
    print(f'Titular da Conta: {self.titulares}') 
    print(f'Saldo da Conta: {self.saldo}')
  
  def extrato(self):
    print(self.operacoes)

class ContaEspecial(ContaBancaria):
  def __init__(self, numero_conta, titulares, saldo, limite = 0):
    ContaBancaria.__init__(self, numero_conta, titulares,saldo)
    self.limite = saldo * 0.15
  def saque(self, valor):
    if valor <= self.saldo:
      self.saldo -= valor
      self.operacoes.append(['Saque', valor, self.saldo])
    elif valor <= self.saldo+self.limite:
      self.saldo -= valor
      self.operacoes.append(['Saque', valor, self.saldo])
      print('Cheque Especial')
    else:
      print('Da não')
      

c1 = ContaEspecial('Anthony',90,100)
c1.resumo_conta()
c1.saque(10)
c1.extrato()




 