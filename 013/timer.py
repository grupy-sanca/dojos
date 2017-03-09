"""
Decorador que imprime tempo de execução de uma função
"""

from fib4 import fib
import time


def timeit(func):
    def wrapper(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        t1 = time.time()
        print('A função levou {}s para executar'.format(t1 - t0))
        return result
    return wrapper


fib = timeit(fib)
fib(50)
