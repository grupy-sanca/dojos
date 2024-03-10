"""
Você recebe duas listas de números inteiros sem repetição.
Escreva uma função que retorne True se as duas listas, quando combinadas,
formam uma sequência consecutiva.
Uma sequência é dita consecutiva quando ela possui todos os valores inteiros entre
seu início e fim, sem buracos.

Exemplos:
- [1, 2, 3, 4, 5] é uma sequência consecutiva.
- [1, 2, 4, 5, 6] não é uma sequência consecutiva, pois há um buraco (falta o número 3)

- combinar([7, 4, 5, 1], [2, 3, 6]) --> True
- combinar([7, 4, 5, 1], [2, 3, 8]) --> False
- combinar([7, 4, 5, 2], [2, 3, 6]) --> True
- combinar([], []) --> True
- combinar([1], []) --> True

>>> verifica_sequencia([1, 2, 3, 4, 5])
True

>>> verifica_sequencia([1, 2, 4, 5, 6])
False

>>> juntar_listas([7, 4, 5, 1], [2, 3, 6])
[7, 4, 5, 1, 2, 3, 6]

>>> juntar_listas([7, 4, 5, 2], [2, 3, 6])
[7, 4, 5, 2, 2, 3, 6]

>>> combinar([7, 4, 5, 1], [2, 3, 6])
True

>>> combinar([7, 4, 5, 1], [2, 3, 8])
False

>>> combinar([7, 4, 5, 2], [2, 3, 6])
True

>>> tratamento_lista([7, 4, 5, 1, 2, 3, 6])
[1, 2, 3, 4, 5, 6, 7]

>>> tratamento_lista([7, 4, 5, 2, 2, 3, 6])
[2, 3, 4, 5, 6, 7]

>>> combinar ([1], [])
True

>>> combinar ([], [])
True
"""

def verifica_sequencia(lista):
    if not lista:
        return True 

    return list(range(lista[0], lista[-1] + 1)) == lista
    

def juntar_listas(lista1, lista2):
    res = lista1 + lista2
    return res

def combinar(lista1, lista2):
    res_juntar_lista = juntar_listas(lista1,lista2)
    res_tratamento_lista = tratamento_lista(res_juntar_lista)
    res_verificar_sequencia = verifica_sequencia(res_tratamento_lista)
    return res_verificar_sequencia 

def tratamento_lista(lista_juntada):
    return list(set(lista_juntada))
