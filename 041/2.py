"""
https://www.codewars.com/kata/526571aae218b8ee490006f4

Write a function that takes an integer as input, and returns the number of bits that are
equal to one in the binary representation of that number. You can guarantee that input
is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should
return 5 in this case.

>>> count(10)
2

>>> count(1234)
5

>>> count(0)
0

>>> count(1)
1

>>> count(2)
1

>>> count(3)
2

>>> count(2**64-1)
64
"""

from collections import Counter

def count(n):
    #return sum([int(bit) for bit in bin(n)[2:]])
    #return bin(n).count('1')
    return Counter(bin(n))['1']
