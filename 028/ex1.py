"""
Dado uma palavra inicial, retornar verdadeiro ou falso se uma segunda palavra é anagrama dela

>>> testa_anagrama("aa", "aa")
True

>>> testa_anagrama("aa", "ab")
False

>>> testa_anagrama("pare", "pera")
True

>>> testa_anagrama("pare", "PERA")
False

>>> testa_anagrama("maçã", "maca")
False
"""

def testa_anagrama(palavra1, palavra2):
    return sorted(palavra1) == sorted(palavra2)