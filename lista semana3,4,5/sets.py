#exercicios de set, semana 2 

#f
#i
#w

f = {'Luis', 'Carlos', 'Fernando', 'Felipe', 'Roger', 'Matheus', 
    'Gabriel', 'Lucas', 'Felipe', 'Roger','Clara', 'Matheus', 'Gabriel', 
    'Lucas','Fernando', 'Felipe', 'Roger', 'Matheus'}

i = {'Luis', 'Carlos', 'Fernando', 'Felipe', 'Roger', 'Matheus', 
    'Gabriel', 'Lucas','Anthony', 'Felipe', 'Roger', 'Matheus', 'Gabriel', 
    'Lucas','Fernando', 'Felipe', 'Roger', 'Matheus'}

w = {'Luis', 'Carlos', 'Fernando', 'Felipe', 'Roger', 'Matheus', 
    'Gabriel', 'Lucas', 'Felipe','Samara', 'Roger', 'Matheus', 'Gabriel', 
    'Lucas','Fernando', 'Felipe', 'Roger','Diego', 'Matheus'}


def calcula_total():
    total = set()
    total.update(f,i,w)
    print(f'O numero total de pessoas que usam alguma rede social é de: {len(total)}')

def calcula_porcentagem():
    porcentagem = (10/30000)*100
    porcentagem = round(porcentagem, 2)
    print(f'{porcentagem}%')


def inter():
    total = f & i & w
    print(len(total))

def dife():
    total = (f | i) - w 
    print(len(total))