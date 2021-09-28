"""
    Problema: https://www.hackerrank.com/challenges/triangle-quest-2/problem

    Exemplo de entrada:
    5

    Exemplo de saída:
    1
    121
    12321
    1234321
    123454321

    ->
    [1, 121, 12321, 1234321, 123454321]

>>> cria_elemento_linha(1)
'1'

>>> cria_elemento_linha(2)
'121'

>>> cria_elemento_linha(3)
'12321'

>>> cria_elemento_linha(4)
'1234321'

>>> cria_lista_palindromos(5)
['1', '121', '12321', '1234321', '123454321']
"""

def cria_elemento_linha(n):
    # 1 * 1 = 1
    # 11 * 11 = 121
    # 111 * 111 = 12321

    primeira_metade = ''
    for i in range(1, n + 1):
        primeira_metade += str(i)
    segunda_metade = primeira_metade[::-1]
    return primeira_metade + segunda_metade[1:]


def cria_lista_palindromos(n):
    lista = []
    for i in range(1, n+1):
        lista.append(str(((10**i)//9)**2))
        #lista.append(str(int(i * "1") ** 2))
    return lista