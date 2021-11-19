"""
https://www.codewars.com/kata/5842df8ccbd22792a4000245

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'

>>> forma_expandida(1)
'1'

>>> forma_expandida(12)
'10 + 2'

>>> forma_expandida(70304)
'70000 + 300 + 4'
"""

def forma_expandida(numero):
    lista_resultado = []  # [digito.ljust(pos, "0") for pos, digito in enumerate(str(numero)[::-1], 1) if digito != "0"]
    for pos, digito in enumerate(str(numero)[::-1], 1):
        if digito == "0":
            continue
        lista_resultado.append(digito.ljust(pos, "0"))  # digito * 10 ** pos

    return ' + '.join(lista_resultado[::-1])