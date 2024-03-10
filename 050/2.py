"""
Encontrar Todas as Anagramas em uma String:
Dado uma string `s` e uma string não vazia `p`, encontre todos os índices iniciais das anagramas de
`p` em `s`. A ordem da saída não importa.

Exemplo:
- Entrada: s = "cbaebabacd", p = "abc"
- Saída: [0, 6]

>>> quebra_em_lista("bigger", 3)
['big', 'igg', 'gge', 'ger']

>>> quebra_em_lista("bigger", 5)
['bigge', 'igger']

>>> encontra_anagrama("bigger", "gig")
[1]

>>> encontra_anagrama("cbaebabacd", "abc")
[0, 6]

>>> encontra_anagrama("cbaebabacd", "fabc")
[]
"""

def quebra_em_lista(string, n):
    substrings = []
    for i in range(len(string) - n + 1):
        substrings.append(string[i:i+n])
    return substrings


def conta_letras(palavra):
    return {letra: palavra.count(letra) for letra in palavra}


def verifica_anagrama(palavra1, palavra2):
    return conta_letras(palavra1) == conta_letras(palavra2)


def encontra_anagrama(s, p):
    substrings = quebra_em_lista(s, len(p))

    resposta = []

    for indice, ss in enumerate(substrings):
        if verifica_anagrama(ss, p):
            resposta.append(indice)

    return resposta
