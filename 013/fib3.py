"""
Fatorial simples com mais linhas

>>> fib(3)
5
>>> fib(4)
8
"""

cache = {}


def cached(func):
    def wrapper(n):
        if n in cache:
            return cache[n]

        result = func(n)
        cache[n] = result
        return result
    return wrapper


def fib(n):
    if n < 2:
        return 1
    return fib(n - 2) + fib(n - 1)


fib = cached(fib)
