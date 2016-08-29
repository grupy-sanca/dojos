"""
Problem: Find the Next Perfect Square

This problem was taken from codewars, you can check it here:
    https://www.codewars.com/kata/56269eb78ad2e4ced1000013
"""

import math


def find_next_square(sq):
    number = math.sqrt(sq)
    if number % 1:
        return -1
    return (number + 1) ** 2
