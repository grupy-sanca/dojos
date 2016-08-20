"""
Um inteiro positivo n é dado. O objetivo do problema é construir a menor
sequencia de inteiros que termina com N de acordo com as seguintes regras:

1. o primeiro elemento da sequencia é 1; A[0] = 1
2. os proximos elementos são gerados pela multiplicação do
elemento anterior por 2 ou somando 1; A[i] = A[i-1] * 2 ou
A[i] = A[i-1] + 1 para i >= 1.
"""


def sequence(length):
    """
    >>> sequence(1)
    1
    >>> sequence(18)
    6
    >>> sequence(36)
    7
    >>> sequence(109)
    11
    """
    count = 0
    while length > 0:
        if length % 2:
            length -= 1
        else:
            length /= 2
        count += 1

    return count
