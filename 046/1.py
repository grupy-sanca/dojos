"""
Crie uma função que recebe uma string como entrada e retorna o primeiro caractere não repetido
na string.

Exemplo:
Entrada: "abracadabra"
Saída: "c"

>>> conta_letra("abracadabra", "a")
5

>>> conta_letra("abracadabra", "b")
2

>>> nao_repete("abracadabra")
'c'

>>> nao_repete("abacaxi")
'b'

>>> nao_repete("aabb")
''
"""

def nao_repete(palavra):
    for i in palavra:
        cont = conta_letra(palavra, i)
        if cont == 1:
            return i
    return ''

def conta_letra(palavra, letra):
    return palavra.count(letra)
