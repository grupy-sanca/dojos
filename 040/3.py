"""
https://www.codewars.com/kata/56a1c074f87bc2201200002e

Write a function that given, an array arr, returns an array containing 
at each index i the amount of numbers that are smaller than arr[i] to the right.

For example:

* Input [5, 4, 3, 2, 1] => Output [4, 3, 2, 1, 0]
* Input [1, 2, 0] => Output [1, 1, 0]

>>> lista_direita(0, [5, 4, 3, 2, 1])
[4, 3, 2, 1]

>>> lista_direita(1, [5, 4, 3, 2, 1])
[3, 2, 1]

>>> conta_menor(5, [4, 3, 2, 1])
4

>>> conta_menor(3, [4, 3, 2, 1])
2

>>> main([5, 4, 3, 2, 1])
[4, 3, 2, 1, 0]

>>> main([1, 2, 0])
[1, 1, 0]
"""


def lista_direita(indice,lista):
    return lista[indice + 1:]

def conta_menor(numero, lista):
    # menores = 0
    # for item in lista:
    #     if item < numero:
    #         menores += 1
    # return menores
    return len([x for x in lista if x < numero])

def main(lista):
    resposta = []
    for i, v in enumerate(lista):
        lista_d = lista_direita(i, lista)
        menor = conta_menor(v, lista_d)
        resposta.append(menor)
    return resposta
