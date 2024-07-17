"""
Verificação de Anagrama:
Escreva uma função que verifica se duas strings de entrada são anagramas uma da outra.
Um anagrama é uma palavra ou frase formada pela reorganização das letras de uma palavra ou frase diferente,
geralmente usando todas as letras originais exatamente uma vez.

Exemplo:
Entrada: ("listen", "silent")
Saída: True

>>> conta_letras("p")
{'p': 1}

>>> conta_letras("palavra")
{'p': 1, 'a': 3, 'l': 1, 'v': 1, 'r': 1}

>>> conta_letras("aaaaa")
{'a': 5}

>>> verifica_anagrama("listen", "silent")
True

>>> verifica_anagrama("ara", "arara")
False




"""

def conta_letras(palavra):
    letras = {}
    for letra in palavra:
        if letra in letras:
            letras[letra] += 1
        else:
            letras[letra] = 1
    return letras


def verifica_anagrama(palavra1, palavra2):
    return conta_letras(palavra1) == conta_letras(palavra2)


