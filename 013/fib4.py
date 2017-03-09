"""
Fatorial simples com mais linhas

>>> fib(3)
5
>>> fib(4)
8
"""

cache = {}


def cached(func):
    def wrapper(*args):
        if args in cache:
            return cache[args]

        result = func(*args)
        cache[args] = result
        return result
    return wrapper


@cached
def fib(n):
    if n < 2:
        return 1
    return fib(n - 2) + fib(n - 1)
