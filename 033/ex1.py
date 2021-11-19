"""
https://www.beecrowd.com.br/judge/pt/problems/view/1168


>>> conta_leds(2819311)
29

>>> conta_leds(23456)
25

>>> conta_leds(115380)
27


>>> resolve_leds(3, [115380, 2819311,  23456])
[27, 29, 25]
"""


def conta_leds(num):
    numero_de_leds = {"1": 2, "2": 5, "3": 5, "4": 4, "5": 5, "6": 6, "7": 3, "8": 7, "9": 6, "0": 6}

    digitos = str(num)
    
    total_leds = 0

    for d in digitos:
        n = numero_de_leds[d]
        total_leds += n
    
    return total_leds

def resolve_leds(total, lista_numeros):
    resultado = []
    for i in range(total):
        resultado.append(conta_leds(lista_numeros[i]))
    return resultado
