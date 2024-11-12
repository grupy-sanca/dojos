
"""
Um número narcisista é um número que é a soma de seus próprios dígitos elevados ao número total
de dígitos. Por exemplo, 153 é um número narcisista, pois 1^3 + 5^3 + 3^3 = 153.
Escreva uma função que verifique se um número é narcisista.

Exemplo:

Entrada:
numero_narcisista(153)

Saída:
True

Entrada:
numero_narcisista(370)

Saída:
True


Entrada:
numero_narcisista(407)

Saída:
True


Entrada:
numero_narcisista(1634)

Saída:
True

Entrada:
numero_narcisista(123)

Saída:
False

>>> numero_narcisista(1)
True

>>> numero_narcisista(10)
False

>>> numero_narcisista(1634)
True
"""

def numero_narcisista(n):
    n_str = str(n)
    l = len(n_str)
    return n == sum(int(digit)**l for digit in n_str)
