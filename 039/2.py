"""
https://www.codewars.com/kata/55960bbb182094bc4800007b

Write a function insert_dash(num) / insertDash(num) / InsertDash(int num)
that will insert dashes ('-') between each two odd digits in num.
For example: if num is 454793 the output should be 4547-9-3.
Don't count zero as an odd digit.

Note that the number will always be non-negative (>= 0).

>>> verificaImpares(23543)
'23-543'

>>> verificaImpares(2543)
'2543'

>>> verificaImpares(454793)
'4547-9-3'

>>> verificaImpares(353793)
'3-5-3-7-9-3'

"""

def verificaImpares(numero):
    impar = "13579"
    res = ""
    anterior_impar = False
    for letter in str(numero):
        if letter in impar:
            if anterior_impar:
                res += "-"
            anterior_impar = True
        else:
            anterior_impar = False
        res += letter
    return res
