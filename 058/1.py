"""
1 - O grupo de pesquisa ResPYre Melhor criou um aplicativo que coletou os dados de cada usuário e colocou em uma lista.
Os dados são: nome (str), idade (int), fumante (bool).
Entretanto, o aplicativo do grupo é bem rudimentar, e acabou agregando os dados dos usuários em listas totalmente desordenadas,
de forma que a lista geral de usuários ficou assim:

usuarios = [
    ['Alberto', 35, True],
    [72, 'Benedita', False],
    [54, True, 'Cecilia'],
    [True, 18, 'Diogo'],
    [False, 'Everton', 27],
    ['Geraldo', True, 64],
    ['Helena', 42, False]
]

Como podemos ver, é muito difícil extrair as as informações de quem é fumante, ou mesmo a idade de cada um.
Vamos auxiliar o pessoal da ResPYre Melhor organizando essa lista deixando todas as entradas de usuarios na forma
[nome, idade, fumante]:

Exemplo:
organizar_usuario([54, True, 'Cecilia'])
['Cecilia', 54, True]

organizar_usuario(['Alberto', 35, True])
['Alberto', 35, True]

Bonus: use a função acima para organizar todos os usuarios de uma vez só
organizar_usuarios([['Alberto', 35, True],[72, 'Benedita', False],[54, True, 'Cecilia'],[True, 18, 'Diogo'],[False, 'Everton', 27],['Geraldo', True, 64],['Helena', 42, False]])
[['Alberto', 35, True],['Benedita', 72, False],['Cecilia', 54, True],['Diogo', 18, True],['Everton', 27, False],['Geraldo', 64, True],['Helena', 42, False]]


>>> organizar_usuario([54, True, 'Cecilia'])
['Cecilia', 54, True]

>>> organizar_usuario(['Alberto', 35, True])
['Alberto', 35, True]

>>> indice('Alberto')
0

>>> indice(True)
2

>>> indice(32)
1

>>> organizar_usuarios([['Alberto', 35, True],[72, 'Benedita', False],[54, True, 'Cecilia'],[True, 18, 'Diogo'],[False, 'Everton', 27],['Geraldo', True, 64],['Helena', 42, False]])
[['Alberto', 35, True], ['Benedita', 72, False], ['Cecilia', 54, True], ['Diogo', 18, True], ['Everton', 27, False], ['Geraldo', 64, True], ['Helena', 42, False]]
"""


def organizar_usuario(dados):
    resposta = [None, None, None]

    for dado in dados:
        resposta[indice(dado)] = dado

    return resposta


def indice(dado):
    if isinstance(dado, str):
        return 0
    elif isinstance(dado, bool):
        return 2
    elif isinstance(dado, int):
        return 1


def organizar_usuarios(lista_usuarios):
    return [organizar_usuario(u) for u in lista_usuarios]
