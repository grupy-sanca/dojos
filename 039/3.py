"""
https://www.codewars.com/kata/55c3026406402936bc000026

This is a follow up from my kata Insert Dashes.
Write a function insertDashII(num) that will insert dashes ('-') between each two odd numbers
and asterisk ('*') between each even numbers in num

For example:
insertDashII(454793) --> 4547-9-3
insertDashII(1012356895) --> 10123-56*89-5

Zero shouldn't be considered even or odd.

>>> insertDashII(454793)
'4547-9-3'

>>> insertDashII(1012356895)
'10123-56*89-5'

>>> insertDashII(4823045)
'4*8*23045'

>>> insertDashII(1000)
'1000'

"""

def insertDashII(num):
    pares = '2468'
    impares = '13579'
    res = ''
    anterior = ''
    for letter in str(num):
        
        if letter in impares:
            if anterior == 'impar':
                res += "-"
            anterior = 'impar'
        elif letter in pares: 
            if anterior == 'par':
                res += '*'
            anterior = 'par'

        else:
            anterior = ''
        res += letter
    return res
