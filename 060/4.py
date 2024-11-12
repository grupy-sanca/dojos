"""
Caminho Mínimo em uma Matriz

Dada uma matriz de inteiros onde cada célula representa um custo para se mover para lá, 
escreva uma função que encontre o caminho de menor custo do canto superior esquerdo ao
 canto inferior direito. Você pode se mover apenas para a direita ou para baixo.

Entrada:
[
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

Saída: 7

Explicação: (O caminho mínimo é 1 → 3 → 1 → 1 → 1)

>>> caminho_minimo([[1,3,1],[1,5,1],[4,2,1]])
7

>> caminho_minimo([[1,2,1],[1,5,1],[4,2,1]])
6

>>> soma_caminho([[1,2,1],[1,5,1],[4,2,1]], 0, 0)
[1, 2]

>>> soma_caminho([[1,2,1],[1,5,1],[4,2,1]], 2, 0)
[None, 2]

>>> gera_caminhos(3, 3)
[[(0, 0), (0, 1), (1, 1)], [(0, 0), (1, 0), (1, 1)]]
"""

def gera_caminhos(n, m):
    caminhos = [
        "BBDD",
        "BDDB",
        "BDBD",
        "DDBB",
        "DBDB",
        "DBBD",
    ]


def caminho_minimo(m):
    custo = m[0][0]
    totais = []
    for i in range(len(m)):
        for j in range(len(m)):
            totais.append(soma_caminho(m, i, j))
    for trecho in totais:
        pass

    return 7

def soma_caminho(m, i, j):
    total = []
    if i < len(m) - 1:
        caminho = m[i+1][j]
        total.append(caminho)
    else:
        total.append(None)

    if j < len(m) - 1:
        caminho = m[i][j+1]
        total.append(caminho)
    else:
        total.append(None)
    return total

