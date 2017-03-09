"""
Fatorial simples com mais linhas

>>> fib(3)
5
>>> fib(4)
8
"""


def fib(n):
    return 1 if n < 2 else fib(n - 2) + fib(n - 1)
