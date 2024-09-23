"""
2 - Quando trabalhamos com valores de cor, pode ser útil extrair os valores individuais dos componentes vermelho, verde e azul
(RGB) para uma cor. Implemente uma função que atenda a esses requisitos:

* Aceita uma string de cor hexadecimal (case-insensitive) como parâmetro (ex. "#FF9933" ou "#ff9933")
* Retorna um dict com a estrutura {"r": 255, "g": 153, "b": 51} onde r, g e b variam de 0 a 255
Observação: sua implementação não precisa suportar a forma abreviada da notação hexadecimal (ou seja, "#FFF")

Exemplo "#FF9933" --> {"r": 255, "g": 153, "b": 51}

>>> decompoe_cor("#FF9933")
{'r': 255, 'g': 153, 'b': 51}

>>> decompoe_cor("#ffffff")
{'r': 255, 'g': 255, 'b': 255}

>>> decompoe_cor("#fff")
{'r': 255, 'g': 255, 'b': 255}

>>> decodifica_cor("F")
255

>>> decodifica_cor("FF")
255

>>> decodifica_cor("99")
153
"""


def decompoe_cor(cor):
    if len(cor) == 7:
        return {'r': decodifica_cor(cor[1:3]), 'g': decodifica_cor(cor[3:5]), 'b': decodifica_cor(cor[5:7])}
    elif len(cor) == 4:
        return {'r': decodifica_cor(cor[1]), 'g': decodifica_cor(cor[2]), 'b': decodifica_cor(cor[3])}


def decodifica_cor(dado):
    if len(dado) == 1:
        dado *= 2
    return int(dado, 16)
