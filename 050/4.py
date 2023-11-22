"""
Você recebe um mapa na forma de uma grade bidimensional de inteiros, 
onde 1 representa terra e 0 representa água. Escreva uma função para
calcular o perímetro da ilha.

Exemplo:
- Entrada:
  
  [[0, 1, 0, 0],
   [1, 1, 1, 0],
   [0, 1, 0, 0],
   [1, 1, 0, 0]]
  

- Saída: 16

>>> add_zeros_h([1])
[0, 1, 0]

>>> padding([[0, 1, 0]])
[[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]

>>> conta_horizontal
"""


def add_zeros_h(lista):
    return [0]+lista+[0]


def padding(matriz):
    matriz = [add_zeros_h(lista) for lista in matriz]
    return [len(matriz[0])*[0]] + matriz + [len(matriz[0])*[0]]
