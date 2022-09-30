"""
In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer

>>> separa_digitos(9119)
[9, 1, 1, 9]

>>> separa_digitos(9229)
[9, 2, 2, 9]


>>> elevaquadrado([9, 1, 1, 9])
[81, 1, 1, 81]

>>> concatena([9, 1, 1, 9])
9119
>>> concatena([9])
9

>>> main(9119)
811181

>>> main(1)
1


"""

def separa_digitos(numero):
    lista = list(str(numero))
    return [int(item) for item in lista]


def elevaquadrado(numeros):
    return[item**2 for item in numeros]

def concatena(numeros):
    return int("".join([str(item) for item in numeros]))

def main(numero):
    digitos = separa_digitos(numero)
    aoquadrado = elevaquadrado(digitos)
    return concatena(aoquadrado)