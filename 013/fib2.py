"""
Fatorial simples com mais linhas

>>> fib(3)
5
>>> fib(4)
8
"""

fibs = {0: 1, 1: 1}


def fib(n):
    if n in fibs:
        return fibs[n]

    result = fib(n - 2) + fib(n - 1)

    fibs[n] = result

    return result
