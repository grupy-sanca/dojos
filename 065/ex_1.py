"""
Crie uma função que recebe uma lista de inteiros e retorna a multiplicação alternada deles,
isto é, a multiplicação de todos os elementos da lista, um a um, alternando o sinal a cada novo elemento.

Por exemplo:
A multiplicação alternada de [3, 4, 5, 6] é:
3 * (-4) * 5 * (-6) = 360


alternate_multiplication([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
-3628800

alternate_multiplication([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8])
3888000

>>> alternate_multiplication([1, 2])
-2

>>> alternate_multiplication([2, 3])
-6

>>> alternate_multiplication([1, 2, 3, 4])
24

>>> alternate_multiplication([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
-3628800

>>> alternate_multiplication([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8])
3888000
"""
from functools import reduce
from operator import mul
def alternate_multiplication(numeros):
    # multiplicação = 1

    # for indice, numero in enumerate(numeros):
    #     multiplicação *= numero if indice % 2 == 0 else -numero
    multiplicação = reduce(mul, [numero if indice % 2 == 0 else -numero for indice, numero in enumerate(numeros)])
    return multiplicação