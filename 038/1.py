"""
https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097

The first century spans from the year 1 up to and including the year 100, the second century
from the year 101 up to and including the year 200, etc.
Task:
Given a year, return the century it is in.
Examples

1705 --> 18
1900 --> 19
1601 --> 17
2000 --> 20

>>> seculo(1705)
18
>>> seculo(1601)
17
>>> seculo(1600)
16
>>> seculo(100)
1
>>> seculo(2000)
20
>>> seculo(10000)
100
>>> seculo(10001)
101
>>> seculo(10)
1
>>> seculo(1)
1
>>> seculo(777777)
7778
"""

def seculo(ano):
    return ((ano - 1) // 100) + 1

    # ano = str(ano)
    # if len(ano) < 3: # entre 0 e 99
    #     return 1

    # fim = ano[-2:]
    # começo = ano[:-2]
    # if fim == "00":
    #     return int(começo)
    # return int(começo) + 1
