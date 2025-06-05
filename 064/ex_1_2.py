"""
1.2 Carrinho de Compras - Desconto

Você foi encarregado de criar uma função que calcula o custo total dos itens em um carrinho de compras.
O carrinho pode conter vários itens, e diversas condições podem afetar o preço final, como descontos e impostos.

Calcule:
    Desconto Percentual:
        Aplique um desconto percentual (ex: 10%) ao preço total do carrinho.

Obs:
Lide com um carrinho vazio de forma adequada.


Caso 1: Carrinho com desconto percentual

Entrada:
items = [
    {"item": "maçã", "preço": 1.0, "quantidade": 3},
    {"item": "banana", "preço": 0.5, "quantidade": 6}
]
desconto = 10  # 10% de desconto

Saída:
5.4

Teste:
calcula_total_com_desconto([{"item": "maçã", "preço": 1.0, "quantidade": 3}, {"item": "banana", "preço": 0.5, "quantidade": 6}], 10)
5.4

>>> calcula_total_com_desconto([{"item": "maçã", "preço": 1.0, "quantidade": 3}, {"item": "banana", "preço": 0.5, "quantidade": 6}], 10)
5.4

>>> calcula_total_com_desconto([{"item": "maçã", "preço": 1.0, "quantidade": 3}, {"item": "banana", "preço": 0.5, "quantidade": 6}], 110)
0.0


>>> calcula_total_com_cupons([{"item": "maçã", "preço": 1.0, "quantidade": 3}, {"item": "banana", "preço": 0.5, "quantidade": 6}], [10,15,25])
3.0
"""
from ex_1_1 import calcula_total_basico


def calcula_total_com_desconto(items, discount):
    discount = min(discount, 100)
    discount_factor = (1 - discount / 100)
    return calcula_total_basico(items) * discount_factor


def calcula_total_com_cupons(items, cupons):
    total_discount = sum(cupons)
    return calcula_total_com_desconto(items, total_discount)
