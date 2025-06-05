"""
1.1 Carrinho de Compras - Básico

Você foi encarregado de criar uma função que calcula o custo total dos itens em um carrinho de compras.
O carrinho pode conter vários itens, e diversas condições podem afetar o preço final, como descontos e impostos.

Calcule:
    Total Básico:
        Calcule o preço total de todos os itens no carrinho.
        Cada item tem um nome, quantidade e preço por unidade.

Obs:
Lide com um carrinho vazio de forma adequada.


Caso 1: Carrinho com um único item (sem descontos ou impostos)

Entrada:
items = [{"item": "maçã", "preço": 1.0, "quantidade": 3}]

Saída:
3.0

Teste:
calcula_total_basico([{"item": "maçã", "preço": 1.0, "quantidade": 3}])
3.0


Caso 2: Carrinho com vários items (sem descontos ou impostos)

Entrada:

items = [
    {"item": "maçã", "preço": 1.0, "quantidade": 3},
    {"item": "banana", "preço": 0.5, "quantidade": 5},
    {"item": "laranja", "preço": 2.0, "quantidade": 2}
]

Saída:
9.5

Teste:
calcula_total_basico([{"item": "maçã", "preço": 1.0, "quantidade": 3}, {"item": "banana", "preço": 0.5, "quantidade": 5}, {"item": "laranja", "preço": 2.0, "quantidade": 2}])
9.5


Caso 3: Carrinho vazio

Entrada:
items = []

Saída:
0

Teste:
>>> calcula_total_basico([])
0.0

>>> calcula_total_basico([{"item": "maçã", "preço": 1.0, "quantidade": 3}])
3.0

>>> calcula_total_basico([{"item": "maçã", "preço": 1.0, "quantidade": 3}, {"item": "banana", "preço": 0.5, "quantidade": 5}, {"item": "laranja", "preço": 2.0, "quantidade": 2}])
9.5

>>> calcula_total_basico([{"item": "maçã", "preço": 1, "quantidade": 3}])
3.0

>>> calcula_total_basico([{"item": "maçã", "preço": 1.0, "quantidade": 0}])
0.0

>>> calcula_total_basico([{"item": "maçã", "preço": "1.0", "quantidade": 0}])
0.0

>>> calcula_total_basico([{"item": "maçã", "preço": "one", "quantidade": 0}])
bad number
"""
def calcula_total_basico(items):
    total = float(0.0)
    try:
        for item in items:
            total += float(item.get("preço")) * float(item.get("quantidade"))
        return total
    except ValueError as err:
        print("bad number")

   
