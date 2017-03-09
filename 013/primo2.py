"""
Memoização (cache)

>>> eh_primo(1)
False
>>> eh_primo(10007)
True
>>> eh_primo(900149)
True
>>> eh_primo(999983)
True
>>> eh_primo(16769023)
True
>>> eh_primo(27644437)
True
"""

primos = {1: False}


def eh_primo(numero):
    if numero in primos:
        return primos[numero]

    for divisor in range(2, numero):
        if numero % divisor == 0:
            primos[numero] = False
            return False

    primos[numero] = True
    return True
