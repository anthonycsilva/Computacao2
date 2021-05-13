import numpy as np
from numpy.core.fromnumeric import shape

#x = np.array([1,2,3]) #criando o um array com os numeros inteiros 1,2 e 3.

y = np.array([[1.,0.,0.], [0.,1.,2.]]) #criando uma array com 2 dimensoes, linha e coluna com os numeros do tipo float 1., 0., ...
                                        #detalhe importante é notar que é uma lista maior que comporta 2 listas dentro dela.  [   [],  []  ]
                                        #o numpy faz a mágica de colocar tudo em ordem quando dado o print
                                        #matriz, ou array. 2x3, ou seja 2 eixos ( duas dimensoes, linha e coluna )
                                        #tipo: numpy.ndarray


#print(y[0])#acessa o primeiro eixo 
#print(y[1])#acessa o segundo eixo

#print(y[1][2]) #acessando um elemento específico


#print(y.shape) #retona as dimensoes do array, como tupla
#shape tbm pode ser usado para reorganizar array já existente da forma que for melhor, porém deve manter o MESMO NUMERO DE ELEMENTOS



#y.shape = (3,2)
#print(y)


#exercício da aula 

#dado um array qualquer, faça uma função que retorne a média de todos os números do array

def mediaArray(array):
    shape_antigo = array.shape
    total_elementos = 1
    for dimensao in array.shape: #verifica o numero do shape (,  ,  )
        total_elementos *= dimensao
    array.shape = (total_elementos,) #cria uma tupla com o total os elementos da array dentro de uma lista

    soma=0
    for elemento in array:
        soma+= elemento
    array.shape = shape_antigo
    return soma/total_elementos

    #feito assim, eu altero o tipo da array que foi inserida
    #com o shape_antigo salvando como ele era antes, é da um novo shape para o formato antigo, assim voltando ao array original


#ESPECIFICANDO TIPOS EM ARRAYS

#NUMPY dtypes
# float64 = numeros de ponto flutuantes de 64bits
# int64 = inteiros de 64 bits
# bool = True ou False ( 8bits )
# outros tipos: complexfloat, signedinteger, ...

# O tipo de dado pode ser definido explicitamente na crianção do array:

x1 = np.array([[1,2,3],[4,5,6]], dtype ='int32')
#print(x1)

x2 = np.array([[1,2,3],[4,5,6]], dtype ='bool')# True para qualquer coisa diferente de 0
#print(x2)

#CRIANDO MATRIZES COM NUMPY

# np.zeros = cria uma array com todos os elementos sendo 0
# np.ones = cria uma array com todos os elementos sendo 1
# np.empty = cria uma array cujo conteúdo inicial é ALEATÓRIO

a = np.zeros(10)
#print(a) # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

#aplicando shape 

a = np.zeros(12)
a.shape = (3,4)
#print(a)

#outro método de aplicação de shape

a = np.zeros((3,4), dtype='int32')
#print(a)

#curiosidade: np.random.random((2,3))

#exercícios 2 da aula
#Crie um arraz de inteiros de 32 bits de formato (3,2,5), no qual todos os elementos são iguais a 3

tres = np.ones((3,2,5), dtype='int32') * 3
#print(tres)

# operadores, +,-,*,/ e ** são aplicados em cada par de elementos dos array, inclusive somando vetores.
# o operador para multiplicação de matrizes é o @ 
# a única restrição é que na operação o numero de linhas e de colunas devem ser iguais para as 2 ou mais matrizes
# é possível também multiplicar um array por uma lista ou tupla
# A @ [0,1]

#CRIANDO SEQUENCIA DE NUMEROS
# np.arange([start], stop, [step], dtype=None)

a = np.arange(10,30,5) # começa no 10, termina no 30, e vai de 5 em 5, mas não inclui o 30 ( aceita argumento float tranquilamente )
#print(a)


#Quando os argumentos de arange são do tipo float, geralmente não é possível prever o número de elementos obtidos.
#Neste caso o melhor é usar a função linspace que recebe como argumento o número de elementos que queremos ao inves do tamanho do passo!

a = np.linspace(0,2,9) # faça de 0 até 2 sendo cortado em 9 partes, ( intervalo fechado nas 2 pontas)
#print(a)


#exercício da aula
#1. faça uma função que dado um intervalo fechado [a,b] e um número de pontos n, retorna dois arrays x e y. 
# x é formado pelos n pontos obtidos a partir do intervalo [a.b] e y é dado por y = x² - 9

def calculaParabola(a,b,n):
    x = np.linspace(a,b,n)
    y = x**2 - 9 # precedencia já é aplicado aqui
    return x, y 

x,y = calculaParabola(0,1,10)


#2. Faça uma função gera_matriz que recebe como parâmetros de entrada (a,b,n,m) e que tem como retorno um array Numpy
# de formato M x M, onde os elementos são os numeors igualmente espaçados obtidos ao se dividir o intervalo [a,b]
# Caso não seja possível construir tal array, a função deve retornar a mensagem Não é possível construir!!

def gera_matriz(a, b, n, m):
    x = np.linspace(a,b,n)
    if m**2 == n:
        x.shape = (m,m)
        return x
    else:
        return('Não é possível construir')


#print(gera_matriz(0,10,10,4))


#EXTRAINDO ELEMENTOS !
# Podemos extrair elementos de linhas e colunas de uma matriz

x = np.array([[1,2],[3,4]])
#print(x[0, :]) # mostra a primeira linha com todas as colunas
#print(x[:,1]) # mostra a coluna desejada com todas as linhas da mesma

# válido para várias dimensões de matrizes

# podemos extrair elementos usando um array como indice

c = np.linspace(2,4,5)
indices = np.array([0,2,3]) 
#print(c[indices]) # pega dentro do array c, os numeros com as coordenadas 0, 2, e 3

# fatiação de aplica nisso também

#PODE SER FEITO USANDO BOOL

indices = np.array([0,1,1,0,0], dtype='bool')
print(c[indices]) # vai mostrar somente o que for True