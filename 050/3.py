"""
https://www.codewars.com/kata/5914e068f05d9a011e000054

Ele recebe uma string:
string="aaaaaaaabaaaa"
E gera um array que soma todos os caracteres repetidos assim:
compressed=[[8,"a"],[1,"b"],[4,"a"]]
A versão compactada é transformada em uma string:
compressed='[[8,"a"],[1,"b"],[4,"a"]]'

Finalmente,
Se a versão compactada for mais curta do que a string original,
a função retornará a versão compactada.
Caso contrário, retornará a string original.

Exemplo1:
string1="aaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaa"
output1='[[26,"a"],[1,"b"],[18,"a"]]'

Exemplo2:
string2="abcde"
output2="abcde"

Após criar o algoritmo de compressão, crie um algoritmo de descompressão:

Ele recebe uma string (output1, output2, etc.).
Se a string estiver comprimida, retorna a versão descomprimida,
Se estiver descomprimida, retorna a string original inalterada.

>>> compacta("aaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaa")
'[[26,"a"],[1,"b"],[18,"a"]]'

>>> compacta("aaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaa")
'[[26,"a"],[1,"b"],[19,"a"]]'

>>> compacta_string("abcde")
'abcde'

>>> compacta_string("aaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaa")
'[[26,"a"],[1,"b"],[19,"a"]]'


>>> descompacta("abcde")
'abcde'


>>> descompacta('[[26,"a"],[1,"b"],[19,"a"]]')
'aaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaa'
"""

import json


def compacta(palavra):
    counter = 1
    lista_final = []
    for i, j in zip(palavra[:-1], palavra[1:]):
        if i == j:
            counter += 1
        else:
            lista_final.append([counter, i])
            counter = 1
    lista_final.append([counter, i])
    resposta = json.dumps(lista_final)
    return resposta.replace(" ", "")


def compacta_string(palavra):
    compactada = compacta(palavra)
    if len(compactada) < len(palavra):
        return compactada
    return palavra


def descompacta(compactada):
    if compactada[0] != '[':
        return compactada
    return ''.join(j*i for i, j in json.loads(compactada))
