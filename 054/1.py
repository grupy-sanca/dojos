"""
1 - Em Biologia, o DNA é uma molécula muito especial.
Nela estão codificadas as instruções para construir proteínas, as quais são indispensáveis
para todos os seres que habitam no planeta.
Essa codificação é dada pela ligação de pontes de hidrogênio formadas entre pares de bases hidrogenadas.
As bases presentes em uma sequência de DNA são a Adenina (A), Citosina (C), Guanina (G) e Timina (T).

Vamos criar uma função que gere uma sequência de DNA que tenha X caracteres.
Essa sequência deve alternar sempre seguindo a ordem: A, C, G, T.

Exemplos:
gerar_dna(3) --> ['A', 'C', 'G']
gerar_dna(9) --> ['A', 'C', 'G', 'T', 'A', 'C', 'G', 'T', 'A']
gerar_dna(0) --> []

>>> gerar_dna(3)
['A', 'C', 'G']

>>> gerar_dna(9)
['A', 'C', 'G', 'T', 'A', 'C', 'G', 'T', 'A']

>>> gerar_dna(0)
[]

>>> gerar_dna(1)
['A']

>>> gerar_dna_com_lista(3)
['A', 'C', 'G']
"""
from time import time

def gerar_dna(tamanho: int) -> list[str]:
    bases = ['A', 'C', 'G', 'T']
    # response = []

    # for idx in range(tamanho):
    #     response.append(bases[idx % len(bases)])

    # list = response.append()

    return bases * (tamanho // len(bases)) + bases[:tamanho % len(bases)]


def gerar_dna_com_lista(tamanho: int) -> list[str]:
    bases = ['A', 'C', 'G', 'T']
    # response = []

    # for idx in range(tamanho):
    #     response.append(bases[idx % len(bases)])

    # return response

    return [bases[indice % len(bases)] for indice in range(tamanho)]


# tamanho = 50000000

# time_ini = time()
# gerar_dna(tamanho)
# time_final = time()
# print(time_final - time_ini)

# time_ini = time()
# gerar_dna_com_lista(tamanho)
# time_final = time()
# print(time_final - time_ini)
