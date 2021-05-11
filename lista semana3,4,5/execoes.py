class NumeroPar(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class NumeradorZero(Exception):
    def __init__(self, msg):
        super().__init__(msg)



def div():
    numerador = float(input('Digite o Numerador: '))
    denominador = float(input('Digite o Denominador: '))

    

    if numerador ==0:
        raise NumeradorZero('A Questão pede que o numerador deve ser diferente de ZERO')

    if int(numerador/denominador)%2 == 0:
        raise NumeroPar('Resultado inteiro é par')

    if denominador ==0:
        raise ZeroDivisionError('O denominador deve ser diferente de ZERO')
    else:
        resultado = numerador/denominador
        resultado = round(resultado, 2)
        print(resultado)
        return resultado




def testa():
    try:
        div()
    except ValueError:
        print('Erro no valor digitado')
    except NumeradorZero:
        print('A questão pede que o numerador seja diferente de ZERO')
    except ZeroDivisionError:
        print('O denominador deve ser diferente de 0')
    except NumeroPar:
        print('A questão pede que o resultado não seja PAR')


testa()