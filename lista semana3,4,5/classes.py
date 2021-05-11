from datetime import date

class Pessoa:
    def __init__(self, nome, nome_social, sobrenome, idade, civil):
        self.nome = nome
        self.nome_social = nome_social
        self.sobrenome = sobrenome
        self.idade = idade
        self.civil = civil

    def setNomeSocial(self, nome_novo):
        print(f'Nome social trocado de {self.nome_social}, para {nome_novo}')
        self.nome_social = nome_novo
    
    def setAniversario(self, data):
        ano = int(data[6:])
        ano_atual = 2021
        self.idade = (ano_atual - ano) 
        print(self.idade)

    def setEstadoCivil(self, novo_civil):
        if self.civil == novo_civil:
            print('Erro. O dado atual é igual ao novo')
        else:
            self.civil = novo_civil
            print(f'Novo estado civil: {self.civil}')


class PessoaFisica(Pessoa):
    def __init__(self,nome, nome_social, sobrenome, idade, civil, cpf, rg):
        Pessoa.__init__(self, nome, nome_social, sobrenome, idade, civil)
        self.cpf = cpf
        self.rg = rg

class PessoaJuridica(Pessoa):
    def __init__(self,nome, nome_social, sobrenome, idade, civil, cnpj):
        Pessoa.__init__(self, nome, nome_social, sobrenome, idade, civil)
        self.cnpj = cnpj
      

class Empregado(PessoaFisica):
    def __init__(self, nome, nome_social, sobrenome, idade, civil, cpf, rg, salario):
        PessoaFisica.__init__(self, nome, nome_social, sobrenome, idade, civil, cpf, rg)
        self.salario = salario

    def aumentaSalario(self, aumento):
        self.salario += aumento
        
    
    def totalAnual(self):
        print(f'Total no ano: {self.salario*13}')
        

        