"""
https://www.codewars.com/kata/5f849ab530b05d00145b9495/train/python

This kata is a slightly harder version of Gravity Flip. It is recommended to do that first.

Bob is bored in his physics lessons yet again, and this time, he's brought a more complex gravity-changing box with him. It's 3D, with small cubes arranged in a matrix of n×m columns. It can change gravity to go in a certain direction, which can be 'L', 'R', 'D', and 'U' (left, right, down, and up).

Given the initial configuration of the cubes inside of the box as a 2D array, determine how the cubes are arranged after Bob switches the gravity.

See the sample tests for examples.
 input =  [[1, 3, 2],
           [4, 5, 1],
           [6, 5, 3],
           [7, 2, 9]]
R -> [[1, 2, 3],
      [1, 4, 5],
      [3, 5, 6],
      [2, 7, 9]]

L -> [[3, 2, 1],
      [5, 4, 1],
      [6, 5, 3],
      [9, 7, 2]]

U -> [[7, 5, 9],
      [6, 5, 3],
      [4, 3, 2],
      [1, 2, 1]]

D -> [[1, 2, 1],
      [4, 3, 2],
      [6, 5, 3],
      [7, 5, 9]]

>>> direita([[1, 3, 2],[4, 5, 1],[6, 5, 3],[7, 2, 9]])
[[1, 2, 3], [1, 4, 5], [3, 5, 6], [2, 7, 9]]

>>> direita([[1, 4, 2],[4, 5, 1],[6, 5, 3],[7, 2, 8]])
[[1, 2, 4], [1, 4, 5], [3, 5, 6], [2, 7, 8]]

>>> esquerda([[1, 3, 2],[4, 5, 1],[6, 5, 3],[7, 2, 9]])
[[3, 2, 1], [5, 4, 1], [6, 5, 3], [9, 7, 2]]

>>> esquerda([[1, 3, 2],[4, 5, 1],[6, 5, 3],[7, 2, 8]])
[[3, 2, 1], [5, 4, 1], [6, 5, 3], [8, 7, 2]]

>>> transposta([[1, 2], [3, 4]])
[[1, 3], [2, 4]]

>>> transposta2([[1, 2], [3, 4]])
[[1, 3], [2, 4]]

>>> cima([[1, 3, 2],[4, 5, 1],[6, 5, 3],[7, 2, 9]])
[[7, 5, 9], [6, 5, 3], [4, 3, 2], [1, 2, 1]]

>>> cima([[1, 3, 2],[4, 5, 1],[6, 5, 3],[7, 2, 8]])
[[7, 5, 8], [6, 5, 3], [4, 3, 2], [1, 2, 1]]

>>> baixo([[1, 3, 2],[4, 5, 1],[6, 5, 3],[7, 2, 9]])
[[1, 2, 1], [4, 3, 2], [6, 5, 3], [7, 5, 9]]

>>> baixo([[1, 3, 2],[4, 5, 1],[6, 5, 3],[7, 2, 8]])
[[1, 2, 1], [4, 3, 2], [6, 5, 3], [7, 5, 8]]
"""

def direita(matriz):
    matriz_direita = []
    for lista in matriz:
        matriz_direita.append(sorted(lista))
    return matriz_direita

def esquerda(matriz):
    matriz_esquerda = []
    for lista in matriz:
        matriz_esquerda.append(sorted(lista, reverse=True))
    return matriz_esquerda

def transposta2(matriz):
    transposta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
    return transposta

def transposta(matriz):
    transposta = []
    for i in range(len(matriz[0])):
        transposta.append([])
        for j in range(len(matriz)):
            transposta[i].append(0)

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            transposta[j][i] = matriz[i][j]
    
    return transposta

def cima(matriz):
    matriz_cima = []
    matriz_transposta = transposta2(matriz)
    for lista in matriz_transposta:
        matriz_cima.append(sorted(lista, reverse=True))
    return transposta2(matriz_cima)

def baixo(matriz):
    matriz_baixo = []
    matriz_transposta = transposta2(matriz)
    for lista in matriz_transposta:
        matriz_baixo.append(sorted(lista))
    return transposta2(matriz_baixo)