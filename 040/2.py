"""
https://www.codewars.com/kata/578aa45ee9fd15ff4600090d
You will be given an array of numbers. You have to sort the odd numbers in ascending order
while leaving the even numbers at their original positions.
Examples

[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

>>> extrai_impar([3, 8, 6, 5, 4])
[3, 5]

>>> extrai_impar([3, 7, 6, 5, 4])
[3, 7, 5]

>>> juntalistas([3, 7, 5],[3, 7, 6, 5, 4])
[3, 5, 6, 7, 4]

>>> juntalistas([3, 7, 7],[3, 7, 6, 7, 4])
[3, 7, 6, 7, 4]

>>> ordenaImparLista([7, 1])
[1, 7]

>>> ordenaImparLista([5, 8, 6, 3, 4])
[3, 8, 6, 5, 4]

>>> ordenaImparLista([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
[1, 8, 3, 6, 5, 4, 7, 2, 9, 0]


"""


def extrai_impar(lista):
    return [numero for numero in lista if numero % 2 == 1]

def juntalistas(l_impares,lista):
    l_impares.sort(reverse = True)
    for i in range(len(lista)):
        if lista[i] %2!=0:
            lista[i]= l_impares.pop()
    return lista

def ordenaImparLista(numeros):
    impares = extrai_impar(numeros)
    return juntalistas(impares, numeros)