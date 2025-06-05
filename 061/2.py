"""
No jogo Campo Minado há 3 tipos de quadrados: quadrados com bombas, quadrados
com números e quadrados vazios.
Os quadrados com números exibem o número de quadrados com bombas que estão à sua volta.
Os quadrados vazios são os que sobram ao preencher todos os quadrados com bombas e os
quadrados com números.

Dada uma matriz que representa um tabuleiro de Campo Minado, sendo a letra B o indicativo
de um quadrado com bomba, preencha seus quadrados com números.

minesweeper(
    [
        ['', 'B', ''],
        ['B', '', ''],
        ['', '', ''],
    ]
)
Retorno:
[
    ['2', 'B', '1'],
    ['B', '2', '1'],
    ['1', '1', ''],
]


>>> minesweeper([['', '', ''],['', '', ''],['', '', '']])
[['', '', ''], ['', '', ''], ['', '', '']]

>>> minesweeper([['B', '', ''],['', '', ''],['', '', '']])
[['B', '1', ''], ['1', '1', ''], ['', '', '']]

>>> minesweeper([['', 'B', ''],['B', '', ''],['', '', '']])
[['2', 'B', '1'], ['B', '2', '1'], ['1', '1', '']]

>>> gera_vizinhos(0, 0, 3, 3)
[(0, 1), (1, 0), (1, 1)]

>>> gera_vizinhos(1, 1, 3, 3)
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]

>>> conta_bombas([['', '', ''],['', '', ''],['', '', '']], (0,0))
0

>>> conta_bombas([['B', '', ''],['', '', ''],['', '', '']], (0, 1))
1

"""

def conta_bombas(campo, pos):
    total_bombas = 0
    vizinhos = gera_vizinhos(pos[0], pos[1], len(campo), len(campo[0]))
    for lin, col in vizinhos:
        if campo[lin][col] == 'B':
            total_bombas += 1
    return total_bombas

def gera_vizinhos(a, b, numlinhas, numcolunas):
    vizinhos = [(a - 1, b - 1), (a - 1, b), (a - 1, b + 1), (a, b - 1), (a, b +1), (a + 1, b - 1), (a + 1, b), (a + 1, b + 1) ]
    vizinhos_validos = []
    for i, j in vizinhos:
        if i < 0 or i >= numlinhas or j < 0 or j >= numcolunas:
            continue
        vizinhos_validos.append((i, j))
    
    return vizinhos_validos
        
def minesweeper(campo):
    for i, linha in enumerate(campo):
        for j, celula in enumerate(linha):
            if celula == 'B':
                continue
            nbombas = conta_bombas(campo, (i,j))
            if nbombas:
                campo[i][j] = str(nbombas)
    return campo