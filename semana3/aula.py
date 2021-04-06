class Cliente:
    def __init__(self, nome_do_cliente, cpf_do_cliente):
        self.nome = nome_do_cliente
        self.cpf = cpf_do_cliente


class ContaBancaria:
    def __init__(self, numero, titulares, saldo = 0):
        self.saldo = saldo
        self.numero = numero
        self.titulares = titulares
        self.lista_operacoes = list()
        print('Conta Aberta')
        self.lista_operacoes.append(['Saldo inicial',0,self.saldo])
    
    def resumo(self):
        print('Conta corrente número: %s Saldo: %10.2f' % (self.numero, self.saldo))
    def saque(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print('Novo saldo: %10.2f' % (self.saldo))
        else:
            print('Erro')
    def lista_titulares(self):
        for pessoas in self.titulares:
            print(pessoas.titulares)
    def adiciona_titular(self, novo_cliente):
        self.titulares.append(novo_cliente)
        print('Cliente Incluído')
    def extrato(self):
        for i in self.lista_operacoes:
            print(i)
  

class ContaEspecial(ContaBancaria):
  def __init__(self, titulares, numero, limite=0, saldo=0):
    ContaBancaria. __init__ (self, numero, titulares, saldo)
    self.limite=limite
  def saque(self,valorsaque):
    if valorsaque <= self.saldo:
      self.saldo-=valorsaque
      self.lista_operacoes.append(["saque",valorsaque,self.saldo])
      print("não ficará negativado")
    elif valorsaque <= self.saldo+self.limite:
      self.saldo-=valorsaque
      self.lista_operacoes.append(["saque", valorsaque, self.saldo])
      print("cheque-especial")
    else:
      print("impossível")
