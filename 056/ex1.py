"""
Dada uma string que contenha números, obter a soma e o produto dos
números inteiros contidos na string.
A função deve receber uma string e retornar uma tupla com o resultado.
Caso a string não possua números, deve-se retonar None e não a tupla.

Exemplos:
a8b2 -> (10, 16)
nnn -> None
a101 1 -> (102, 101)

>>> valor_da_soma("a8n2")
10

>>> valor_da_soma("a8n3")
11

>>> valor_da_soma("a101 1")
102

>>> valor_da_soma("1000")
1000

>>> valor_da_soma("")


>>> valor_da_mul("a8n2")
16

>>> valor_da_mul("a8n3")
24

>>> valor_da_mul("a101 8")
808

>>> valor_da_mul("1")
1

>>> valor_da_mul("8")
8

>>> valor_da_mul("")

>>> resultado("a8b2")
(10, 16)

>>> resultado("a8b3")
(11, 24)

>>> resultado("abc")

>>> resultado("a101 1")
(102, 101)

>>> extrai_numeros("a8b2")
[8, 2]

>>> extrai_numeros("a8b3")
[8, 3]

>>> extrai_numeros("aaaa")
[]

>>> extrai_numeros("")
[]
"""

def valor_da_soma(string):
    numeros = extrai_numeros(string)
    return sum(numeros) if len(numeros) > 0 else None

def valor_da_mul(string):
    numeros = extrai_numeros(string)
    if len(numeros) == 0:
        return None
    resultado = 1
    for valor in numeros:
        resultado *= valor
    return resultado

def resultado(string):
    soma, multi = valor_da_soma(string), valor_da_mul(string)
    if all([soma, multi]):
        return soma, multi
    return

def extrai_numeros(string):
    numeros = []
    atual = ""
    for caracter in string:
        if caracter.isnumeric():
            atual += caracter
        else:
            if atual != "":
                numeros.append(int(atual))
            atual = ""
    if atual != "":
        numeros.append(int(atual))
    return numeros