"""
https://www.codewars.com/kata/5267e5827526ea15d8000708

Pete is now mixing the cake mixture. He has the recipe, containing the required
ingredients for one cake. He also might have added some of the ingredients already,
but something is missing. Can you help him to find out, what he has to add to the
mixture?

Requirements:

    Pete only wants to bake whole cakes. And ingredients, that were added once to
    the mixture, can't be removed from that. That means: if he already added the
    amount of flour for 2.8 cakes, he needs to add at least the amount of flour
    for 0.2 cakes, in order to have enough flour for 3 cakes.
    If Pete already added all ingredients for an integer amount of cakes, you don't
    need to add anything, just return an empty hash then.
    If Pete didn't add any ingredients at all, you need to add all ingredients for
    exactly one cake.
    For simplicity we ignore all units and just concentrate on the numbers. E.g. 250g
    of flour is simply 250 (units) of flour and 1 lb of sugar is also simply 1 (unit)
    of sugar.ingingredienteingredienterediente
    Ingredients, which don't have to be added to the mixture (missing amount = 0),
    must not be present in the result.

Examples:

var recipe = {flour: 200, eggs: 1, sugar: 100};

getMissingIngredients(recipe, {flour: 50, eggs: 1}); // must return {flour: 150, sugar: 100}
getMissingIngredients(recipe, {}); // must return {flour: 200, eggs: 1, sugar: 100}
getMissingIngredients(recipe, {flour: 500, sugar: 200}); // must return {flour: 100, eggs: 3, sugar: 100}

>>> get_missing({'flour': 200}, {})
{'flour': 200}

>>> get_missing({'flour': 200, 'egg': 1}, {'flour': 200})
{'egg': 1}

>>> get_missing({'flour': 200, 'egg': 1}, {'flour': 200, 'egg': 2})
{'flour': 200}

>>> get_missing({'flour': 200, 'eggs': 1, 'sugar': 100}, {'flour': 500, 'sugar': 200})
{'flour': 100, 'eggs': 3, 'sugar': 100}
"""

from math import ceil


def get_missing(receita, quant):
    div = {}
    for ingrediente in receita:
        div[ingrediente] = quant.get(ingrediente, 0) / receita.get(ingrediente)

    max_ = ceil(max(max(div.values()),1))
    dif = {ingrediente: max_ - div[ingrediente] for ingrediente in div}
    x_nome = {ingrediente: receita[ingrediente] * dif[i] for ingrediente, i in zip(receita,dif)}
    return {k: int(v) for k,v in x_nome.items() if v!=0}

    # for ingrediente in receita:
    #    if ingrediente not in quant:
    #        return {ingrediente: receita[ingrediente]}
    #    if quant[ingrediente] < receita[ingrediente]:
    #        return {ingrediente: absreceita[ingrediente] - quant[ingrediente]}
