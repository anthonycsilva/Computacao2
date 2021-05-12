def bbb(frase):
    dicio = dict()
    for letra in frase:
        if letra in dicio:
            dicio[letra] += 1
        else:
            dicio[letra] = 1

    
    print(dicio)


def dic2():
    pessoas = {'nome':'Anthony', 'sexo':'M', 'idade':22}
    pessoas['peso'] = '67'
    #print(f'{pessoas["nome"]}, tem {pessoas["idade"]}')
    #print(pessoas.values())
    #print(pessoas.items())

    for k, v in pessoas.items():
        print(f'{k} = {v}')


bbb('inimigo do meu inimigo, é meu amigo')