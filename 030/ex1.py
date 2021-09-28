"""
https://www.urionlinejudge.com.br/judge/pt/problems/view/1238

Implemente um programa denominado combinador, que recebe duas strings e deve
combiná-las, alternando as letras de cada string, começando com a primeira letra
da primeira string, seguido pela primeira letra da segunda string, em seguida
pela segunda letra da primeira string, e assim sucessivamente. As letras restantes
da cadeia mais longa devem ser adicionadas ao fim da string resultante e retornada.

Exemplo:
2
Tpo oCder
aa bb

Saida:
TopCoder
abab

>>> combine("Tpo", "oCder")
'TopCoder'

>>> combine("aa", "bb")
'abab'

>>> combine("aaaaa", "bbb")
'abababaa'
"""
from itertools import zip_longest

def combine(string_1, string_2):
    final_string = ""
    for s1, s2 in zip_longest(string_1, string_2, fillvalue=""):
        final_string += s1 + s2
    return final_string

# def combine(string_1, string_2):
#     return "".join(
#      [s1 + s2 for s1, s2 in zip_longest(string_1, string_2, fillvalue="")]
#     )


# def combine(string_1, string_2):
#     # A string maior deve permanecer
#     smaller_string_size = min(len(string_1), len(string_2))
#     final_string = ""
#     for i in range(smaller_string_size):
#         final_string += string_1[i]
#         final_string += string_2[i]
#     final_string += string_1[i+1:]
#     final_string += string_2[i+1:]
#     return final_string

    