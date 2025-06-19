"""
Dojo 067 - A Festa Junina

Exercício 1: O Convite Perdido

A Festa Junina está chegando! Mas o convite para a grande festa na fazenda se perdeu.
Felizmente, você encontrou um mapa da cidade onde o convite está marcado com um 'X'.

O mapa é representado por uma grade (uma lista de listas de caracteres).
Sua primeira tarefa é escrever uma função `encontrar_convite(mapa)` que receba o mapa
e retorne as coordenadas (linha, coluna) do convite.

As coordenadas devem ser baseadas em índice 0.

Se não houver convite, a função deve retornar `None`.

Exemplos de Teste:

1.  Mapa simples:
    - Entrada: `mapa = [['O'], ['X'], ['O']]`
    - Saída esperada: `(1, 0)`

2.  Mapa em grade:
    - Entrada: `mapa = [['O', 'O', 'O'], ['O', 'X', 'O'], ['O', 'O', 'O']]`
    - Saída esperada: `(1, 1)`

3.  Mapa sem convite:
    - Entrada: `mapa = [['O', 'O'], ['O', 'O']]`
    - Saída esperada: `None`

4.  Mapa com convite na borda:
    - Entrada: `mapa = [['X', 'O'], ['O', 'O']]`
    - Saída esperada: `(0, 0)`

5.  Mapa com múltiplas ocorrências (a função deve retornar a primeira que encontrar):
    - Entrada: `mapa = [['O', 'X'], ['O', 'X']]`
    - Saída esperada: `(0, 1)`

Agora, mãos à obra! Crie a função `encontrar_convite` e os testes para ela.

>>> encontrar_convite([['O'], ['X'], ['O']])
(1, 0)

>>> encontrar_convite([['O', 'O', 'O'], ['O', 'X', 'O'], ['O', 'O', 'O']])
(1, 1)

>>> encontrar_convite([['O', 'O'], ['O', 'O']])
'Não encontrado'

>>> encontrar_convite([['X', 'O'], ['O', 'O']])
(0, 0)

>>> encontrar_convite([['O', 'X'], ['O', 'X']])
(0, 1)

"""

def encontrar_convite(mapa):
    i=0
    j=0
    for linha in mapa: 
        for coluna in linha:
           if coluna =="X":
                return (i,j)
           j+=1
        i+=1
        j=0
    return "Não encontrado"
        