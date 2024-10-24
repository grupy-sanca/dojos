"""
3) Se fôssemos configurar um jogo da velha, gostaríamos de saber se o estado atual do tabuleiro está resolvido, não é?
Nosso objetivo é criar uma função que verifique isso para nós!

Assuma que o tabuleiro vem na forma de um array 3x3, onde o valor é 0 se uma posição estiver vazia, 1 se for um "X",
ou 2 se for um "O", como neste exemplo:

[[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]

Queremos que nossa função retorne:
    -1 se o tabuleiro ainda não estiver finalizado E ninguém ganhou (existem posições vazias),
    1 se o "X" ganhou,
    2 se o "O" ganhou,
    0 se for um empate (ou seja, um jogo sem vencedor).

Você pode assumir que o tabuleiro passado é válido no contexto de um jogo da velha.

Exemplos:

Entrada:
[[1, 1, 1],
 [0, 2, 0],
 [2, 0, 0]]
Saída: 1

Entrada:
[[2, 1, 0],
 [1, 2, 0],
 [0, 1, 2]]
Saída: 2

Entrada:
[[2, 1, 2],
 [2, 1, 1],
 [1, 2, 1]]
Saída: 0

Entrada:
[[1, 0, 0],
 [0, 2, 0],
 [0, 0, 0]]
Saída: -1

>>> checa_linha([1, 1, 1])
1

>>> checa_linha([2, 2, 2])
2

>>> checa_linha([1, 2, 1])
0

>>> checa_linha([1, 2, 0])
0

>>> verifica_tabuleiro([[1, 1, 1],[0, 2, 0],[2, 0, 0]])
1

>>> verifica_tabuleiro([[2, 1, 0],[2, 0, 1],[2, 1, 2]])
2

# >>> verifica_tabuleiro([[2, 1, 0],[1, 2, 0],[0, 1, 2]])
# 2

"""
def checa_linha(linha):
    if all([a == linha[0] for a in linha]):
        return linha[0]
    return 0

def verifica_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        resultado = checa_linha(linha)
        if resultado > 0:
            return resultado
    for i in range(3):
        for 
        coluna = [tabuleiro[]
