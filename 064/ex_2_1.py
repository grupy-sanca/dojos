"""
2.1 Rotação de Matriz (Sentido Horário)

Escreva uma função para rotacionar uma matriz 2D (NxN) 90 graus no sentido horário.

Passos:
    Valide que a entrada é uma matriz quadrada.
    Transponha a matriz (troque linhas por colunas).
    Inverta cada linha da matriz transposta.

Exemplos:

Entrada:
[
    [1, 2],
    [3, 4],
]

[
    [1, 3]
    [2, 4]
]

Saída:
[
    [3, 1],
    [4, 2]
]confere_quadrado

Teste:
rotaciona_matriz([[1, 2], [3, 4]])
[[3, 1], [4, 2]]


Entrada:
[
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]

Saída:
[
 [7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]
]

Teste:
rotaciona_matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
[[7, 4, 1], [8, 5, 2], [9, 6, 3]]

Entrada:
[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

Saída:
[
    [13, 9, 5, 1],
    [14, 10, 6, 2],
    [15, 11, 7, 3],
    [16, 12, 8, 4]
]

Teste:
rotaciona_matriz([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
[[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]

>>> confere_quadrado([[1, 2], [3, 4]])
True

>>> confere_quadrado([[1, 2]])
False

>>> transpose([[1, 2], [3, 4]])
[[1, 3], [2, 4]]

>>> rotaciona_matriz([[1, 2], [3, 4]])
[[3, 1], [4, 2]]

"""

def confere_quadrado(matrix):
    m = len(matrix)
    for linha in matrix:
        if len(linha) != m:
            return False
    return True


def transpose(matrix):
    if confere_quadrado(matrix):
        dimension = len(matrix)

        transposed = []
        for _ in range(dimension):
            transposed.append([0] * dimension)

        for i in range(dimension):
            for j in range(dimension):
                transposed[i][j] = matrix[j][i]

        return transposed


def rotaciona_matriz(matrix):
    transposed = transpose(matrix)

    for row in transposed:
        row.reverse()
    return transposed
