"""
>>> calcula([1, 2])
4
>>> calcula([1, 3])
8
>>> calcula([5, 8])
12
>>> calcula([8, 5])
12
>>> calcula([8, 5, 8, 7])
28
"""

from functools import reduce


def calculav0(andares):
    soma = 0
    anterior = andares[0]
    for numero in andares[1:]:
       soma += 4 * abs(numero - anterior )
       anterior = numero
    return soma


def calculav1(andares):
    soma = 0
    for anterior, numero in zip(andares[:-1], andares[1:]):
       soma += 4 * abs(numero - anterior )
    return soma


def calcula(andares):
    return 4 * sum(abs(num - ant) for ant, num in zip(andares[:-1], andares[1:]))
