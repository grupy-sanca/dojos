"""
Dojo 067 - A Festa Junina

Exercício 2: A Quadrilha Desorganizada

A quadrilha da festa junina está toda desorganizada! Cada par tem um nome e um número,
mas eles estão em uma ordem aleatória. Sua tarefa é organizar os pares em ordem alfabética
pelo nome.

Escreva uma função `organizar_quadrilha(pares)` que recebe uma lista de tuplas, onde
cada tupla contém um nome (string) e um número (inteiro). A função deve retornar a
lista de tuplas ordenada alfabeticamente pelo nome.

Exemplos de Teste:

1.  Lista de pares desordenada:
    - Entrada: `pares = [("Maria", 3), ("João", 1), ("Ana", 2)]`
    - Saída esperada: `[('Ana', 2), ('João', 1), ('Maria', 3)]`

2.  Lista vazia:
    - Entrada: `pares = []`
    - Saída esperada: `[]`

3.  Lista com nomes iguais (a ordem relativa dos itens com nomes iguais deve ser mantida):
    - Entrada: `pares = [("Pedro", 2), ("Pedro", 1)]`
    - Saída esperada: `[('Pedro', 2), ('Pedro', 1)]`

4.  Lista de pares maior:
    - Entrada: `pares = [("Zé", 5), ("Ana", 1), ("Maria", 3), ("João", 2), ("Pedro", 4)]`
    - Saída esperada: `[('Ana', 1), ('João', 2), ('Maria', 3), ('Pedro', 4), ('Zé', 5)]`

Crie a função `organizar_quadrilha` e os testes para verificar seu funcionamento.

>>> organizar_quadrilha([("Maria", 3), ("João", 1), ("Ana", 2)])
[('Ana', 2), ('João', 1), ('Maria', 3)]

>>> organizar_quadrilha([])
[]

>>> organizar_quadrilha([("Pedro", 2), ("Pedro", 1)])
[('Pedro', 2), ('Pedro', 1)]

>>> organizar_quadrilha([("Zé", 5), ("Ana", 1), ("Maria", 3), ("João", 2), ("Pedro", 4)])
[('Ana', 1), ('João', 2), ('Maria', 3), ('Pedro', 4), ('Zé', 5)]


"""

def organizar_quadrilha(lista):
    lista.sort(key=lambda x: x[0])
    return lista
    
    