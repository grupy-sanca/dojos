"""
Validador de Quadrados Mágicos 3x3
https://www.codewars.com/kata/magic-square-validator/

Recebe da entrada padrão uma matriz de tamanho 3x3...
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

>>> matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> checar_linha([1, 2, 3])
False
>>> checar_linha([4, 9, 2])
True
>>> transpor(matriz)
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
>>> transpor(transpor(matriz))
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> checar_diagonais(matriz)
True
>>> checar_diagonais(transpor(matriz))
True
>>> is_magical(matriz)
False
>>> matriz_magica = [[4,9,2], [3,5,7], [8,1,6]]
"""

from copy import deepcopy


def checar_linha(linha):
    return sum(linha) == 15


def transpor(matriz):
    tam = len(matriz)
    return [[matriz[i][j] for i in range(tam)] for j in range(tam)]
    
    
def checar_diagonais(matriz):
    tam = len(matriz)
    diagonal1 = [matriz[i][i] for i in range(tam)]
    diagonal2 = [matriz[i][tam - 1 - i] for i in range(tam)]
    return sum(diagonal1) == 15 and sum(diagonal2) == 15
    
    

def is_magical(quadrado):
    linhas = [checar_linha(linha) for linha in quadrado]
    colunas = [checar_linha for linha in transpor(quadrado)]
    
    return not all(linhas) and not all(colunas) and checar_diagonais(matriz)
