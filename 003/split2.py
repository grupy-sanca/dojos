"""
Um numero intero x e um array A com N elementos inteiros é dado.
Queremos saber quais elementos de A são iguas a x e quais são diferentes.
O objetivo é dividir o array em duas partes. De tal forma que o numero de
elementos iguais a x na primeira parte seja igual ao numero de elementos
diferentes de x na segunda parte.
"""


def countx(x, l):
    """
    >>> countx(5, [1,5,1,1,1])
    (1, 4)
    """
    count = l.count(x)
    return count, len(l) - count


def split(x, l):
    """
    >>> split(5, [1,5,1,1,1])
    4
    >>> split(5, [5,5,1,2,3,4,5])
    4
    >>> split(5, [5,5,1,2,3,4,5])
    4
    >>> split(5, [1,1,1,2,3,4,1])
    7
    >>> split(5, [5,5,1,7,2,3,5])
    4
    >>> split(5, [5,3,1,7,2,5,5])
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
    curleft = 0
    left, right = countx(x, l)
    curright = right
    for i in range(len(l)):
        if l[i] == x:
            curleft += 1
        else:
            curright -= 1
        if curleft == curright:
            return i + 1
    return len(l)
