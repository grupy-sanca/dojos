"""
https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python


>>> row_sum_odd_numbers(1)
1

>>> sum_up_to(4)
10


>>> n_odd_firsts(1)
[1]
>>> n_odd_firsts(5)
[1, 3, 5, 7, 9]
>>> row_sum_odd_numbers(2)
8
>>> row_sum_odd_numbers(3)
27
>>> row_sum_odd_numbers(41)
68921
"""


def n_odd_firsts(i):
    return list(range(1, i * 2, 2))


def sum_up_to(n):
    i = 0
    while n > 0:
        i += n
        n = n-1
    return i


def row_sum_odd_numbers(n):
    i = sum_up_to(n)
    n_first = n_odd_firsts(i)
    return sum(n_first[-n:])
