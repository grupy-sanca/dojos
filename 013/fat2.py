"""
Fatorial simples com mais linhas

>>> fat(3)
6
>>> fat(5)
120
"""

fatoriais = {1: 1}


def fat(n):
    if n in fatoriais:
        return fatoriais[n]

    result = n * fat(n - 1)
    fatoriais[n] = result
    return result
