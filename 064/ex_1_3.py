"""
1.3 Carrinho de Compras - Impostos

Você foi encarregado de criar uma função que calcula o custo total dos itens em um carrinho de compras.
O carrinho pode conter vários itens, e diversas condições podem afetar o preço final, como descontos e impostos.

Calcule:
    Aplicação de Impostos:
        Adicione uma porcentagem de imposto (ex: 5%) ao preço total, após aplicar os descontos.

Obs:
Lide com um carrinho vazio de forma adequada.


Caso 1: Carrinho com imposto percentual

Entrada:
items = [
    {"item": "maçã", "preço": 1.0, "quantidade": 3},
    {"item": "banana", "preço": 0.5, "quantidade": 6}
]
desconto = 0
impostos = 5  # 5% de imposto

Saída:
5.7

Teste:
calcula_total_com_imposto([{"item": "maçã", "preço": 1.0, "quantidade": 3}, {"item": "banana", "preço": 0.5, "quantidade": 6}], 10)
5.7

>>> calcula_total_com_imposto([{"item": "maçã", "preço": 1.0, "quantidade": 7}, {"item": "banana", "preço": 0.5, "quantidade": 6}], 50, 10)
5.5

>>> calcula_total_com_imposto([{"item": "maçã", "preço": 1.0, "quantidade": 0}], 50, 10)
0.0

>>> calcula_total_com_imposto([{"item": "maçã", "preço": 1.0, "quantidade": 7}, {"item": "banana", "preço": 0.5, "quantidade": 6}], 50, 10)
5.5

>>> calcula_total_com_imposto([{"item": "maçã", "preço": 1.0, "quantidade": 7}, {"item": "banana", "preço": 0.5, "quantidade": 6}], 0, 200)
30.0

>>> calcula_total_com_imposto([{"item": "maçã", "preço": 1.0, "quantidade": 7}, {"item": "banana", "preço": 0.5, "quantidade": 6}], 0, 0)
10.0

>>> calcula_total_com_imposto([{"item": "maçã", "preço": 1.0, "quantidade": 7}, {"item": "banana", "preço": 0.5, "quantidade": 6}], 0, -200)
-10.0
"""
from ex_1_2 import calcula_total_com_desconto


def calcula_total_com_imposto(items, discount, tax):
    total = calcula_total_com_desconto(items, discount)
    return total * (1 + tax / 100)