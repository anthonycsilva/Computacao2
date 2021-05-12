import numpy as np

x = np.array([1,2,3]) #criando o um array com os numeros inteiros 1,2 e 3.

y = np.array([[1.,0.,0.], [0.,1.,2.]]) #criando uma array com 2 dimensoes, linha e coluna com os numeros do tipo float 1., 0., ...
                                        #detalhe importante é notar que é uma lista maior que comporta 2 listas dentro dela.  [   [],  []  ]
                                        #o numpy faz a mágica de colocar tudo em ordem quando dado o print
                                        #matriz, ou array. 2x3, ou seja 2 eixos ( duas dimensoes, linha e coluna )
                                        #tipo: numpy.ndarray


print(y[0])#acessa o primeiro eixo 
print(y[1])#acessa o segundo eixo

print(y[1][2]) #acessando um elemento específico


print(y.shape) #retona as dimensoes do array, como tupla


