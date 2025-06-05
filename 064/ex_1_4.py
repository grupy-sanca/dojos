"""
1.4 Carrinho de Compras - Completo

Você foi encarregado de criar uma função que calcula o custo total dos itens em um carrinho de compras.
O carrinho pode conter vários itens, e diversas condições podem afetar o preço final, como descontos e impostos.

Junte todas as implementações para criar o carrinho completo.


Caso 1: Carrinho com vários itens e diferentes descontos e impostos

Entrada:

items = [
    {"item": "maçã", "preço": 2.0, "quantidade": 4},
    {"item": "pera", "preço": 1.5, "quantidade": 3},
    {"item": "laranja", "preço": 1.2, "quantidade": 5}
]
desconto = 15  # 15% de desconto
impostos = 8  # 8% de imposto

Saída:
16.98

Teste:
calcula_total_completo([{"item": "maçã", "preço": 2.0, "quantidade": 4}, {"item": "pera", "preço": 1.5, "quantidade": 3}, {"item": "laranja", "preço": 1.2, "quantidade": 5}], 15, 8)
16.98
"""
