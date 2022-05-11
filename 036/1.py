"""
https://www.codewars.com/kata/515decfd9dcfc23bb6000006

>>> sobrevive(10, 10)
False

>>> sobrevive(20, 10)
True
"""

def sobrevive(pedra, dragao):
    return pedra >= 2 * dragao
