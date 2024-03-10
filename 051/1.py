"""
Você fica tão feliz no natal que tem vontade de gritar para todo mundo: "Feliz natal!!".
Pra colocar toda essa felicidade pra fora, você montou um programa que, colocado um índice
I de felicidade, seu grito de natal é mais animado.
Entrada

A entrada é composta por um inteiro I (1 < I ≤ 104) que representa o índice de felicidade.
Saída

A saída é composta pela frase "Feliz natal!", sendo repetidas I vezes a última letra a da frase.
Uma quebra de linha é necessária após a impressão da frase.
Exemplo de Entrada
5

Exemplo de Saída
Feliz nataaaaal!
>>> feliz_natal(5)
'Feliz nataaaaal!'

>>> feliz_natal(10)
'Feliz nataaaaaaaaaal!'

>>> feliz_natal(0)
'Feliz natl!'
"""


def feliz_natal(felicidade: int) -> str:
    return f'Feliz nat{"a" * felicidade}l!'
