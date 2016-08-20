"""
Um numero intero x e um array A com N elementos inteiros é dado.
Queremos saber quais elementos de A são iguas a x e quais são diferentes.
O objetivo é dividir o array em duas partes. De tal forma que o numero de
elementos iguais a x na primeira parte seja igual ao numero de elementos
diferentes de x na segunda parte.
"""


def split(x, l):
    """
    >>> split(5, [5,5,1,7,2,3,5])
    4
    >>> split(5, [5,3,1,7,2,5,5])
    4
    >>> split(5, [5,3,1,5,5])
    2
    >>> split(5, [1,3,1,1,1])
    5
    >>> split(5, [5,1,7,2,3,5])
    4
    """
    for pos in range(len(l)):
        left, right = check(l, pos, x)
        if left == right:
            return pos
    return pos + 1


def check(l, pos, x):
    """
    >>> check([5,5,1,7,2,3,5], 1, 5)
    (1, 4)
    >>> check([5,5,1,7,2,3,5], 2, 5)
    (2, 4)
    >>> check([5,5,1,7,2,3,5], 3, 5)
    (2, 3)
    >>> check([5,5,1,7,2,3,5], 4, 5)
    (2, 2)
    >>> check([5,5,1,7,2,3,5], 5, 5)
    (2, 1)
    >>> check([5,5,1,7,2,3,5], 6, 5)
    (2, 0)
    """
    left = l[:pos].count(x)
    right = len(l) - pos - l[pos:].count(x)
    return left, right
