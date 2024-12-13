"""
No jogo Candy Crush, o objetivo é fazer movimentos que gerem combinações.
Um movimento se caracteriza pela troca de posição de dois símbolos adjacentes,
e uma combinação é registrada quando três ou mais símbolos iguais se alinham na
vertical ou horizontal.
Para que uma partida não termine prematuramente, há no jogo uma funcionalidade
extremamente importante: re-embaralhar o tabuleiro caso não haja mais opções de movimentos possíveis.

Crie uma função que receba uma matriz representando um tabuleiro de Candy Crush,
e que retorne se ainda há movimentos disponíveis para serem feitos.

Restrições:
- A matriz é fixa e tem tamanho 5x5
- Somente considere combinações simples de 3 símbolos na horizontal ou vertical

Exemplos:
A seguinte matriz retornaria True, pois ainda há movimentos possíveis.
[
    ['A', 'B', 'C', 'D', 'A'],
    ['B', 'A', 'A', 'B', 'C'],
    ['D', 'C', 'D', 'C', 'D'],
    ['A', 'D', 'B', 'A', 'B'],
    ['C', 'A', 'C', 'C', 'A']
]

A seguinte matriz retornaria False, pois não há movimentos possíveis.
[
    ['C', 'C', 'B', 'D', 'A'],
    ['B', 'A', 'A', 'B', 'C'],
    ['B', 'C', 'D', 'C', 'D'],
    ['A', 'D', 'B', 'A', 'B'],
    ['C', 'A', 'C', 'D', 'A']
]
"""
