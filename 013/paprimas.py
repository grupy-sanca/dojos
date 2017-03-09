"""
Resolução do problema de palavras primas.
Retirado de http://br.spoj.com/problems/PAPRIMAS/

"abc" = (1, 2, 3) -> 6

>>> converte_letra_numero("a")
1
>>> converte_letra_numero("A")
27

>>> converte_palavra_numero("abc")
6

>>> palavra_eh_prima("b")
True

>>> palavra_eh_prima("d")
False

>>> palavra_eh_prima("UFRN")
True

>>> palavra_eh_prima("AcM")
False

>>> palavra_eh_prima("a")
False
"""
import string


def converte_letra_numero(letra):
    lista = string.ascii_letters
    return lista.find(letra) + 1


def converte_palavra_numero(palavra):
    return sum(converte_letra_numero(c) for c in palavra)


def eh_primo(numero):
    if numero <= 1:
        return False

    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False

    return True


def palavra_eh_prima(palavra):
    return eh_primo(converte_palavra_numero(palavra))
