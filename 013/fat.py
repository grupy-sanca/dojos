"""
Fatorial simples

>>> fat(3)
6
>>> fat(5)
120
"""


def fat(n):
    return 1 if n == 1 else n * fat(n - 1)
