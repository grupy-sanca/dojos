"""
>>> sequence(1)
1

>>> sequence(18)
6

>>> sequence(36)
7

>>> sequence(109)
11
"""


def sequence(length):
    count = 0
    while length > 0:
        if length % 2:
            length -= 1
        else:
            length /= 2
        count += 1

    return count
