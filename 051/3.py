"""
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are
12, 38, 15, and 77. Adding these together produces 142.

>>> extracao_numero('1abc2')
12

>>> extracao_numero('pqr3stu8vwx')
38

>>> extracao_numero('a1b2c3d4e5f')
15

>>> solucao(['1abc2', 'pqr3stu8vwx', "a1b2c3d4e5f", 'treb7uchet'])
142

>>> solucao(['pqr3stu8vwx', "a1b2c3d4e5f", 'treb7uchet'])
130
"""


def extracao_numero(frase):
    numeros = [char for char in frase if char.isdigit()]
    return (int(numeros[0] + numeros[-1]))


def solucao(linhas):
    return sum([extracao_numero(palavra) for palavra in linhas])
