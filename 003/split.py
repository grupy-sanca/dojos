"""

>>> check([5,5,1,7,2,3,5], 1, 5)
(1, 4)
>>> check([5,5,1,7,2,3,5], 2, 5)
(2, 4)
>>> check([5,5,1,7,2,3,5], 3, 5)
(2, 3)
>>> check([5,5,1,7,2,3,5], 4, 5)
(2, 2)
>>> check([5,5,1,7,2,3,5], 5, 5)
(2, 1)
>>> check([5,5,1,7,2,3,5], 6, 5)
(2, 0)
>>> split(5, [5,5,1,7,2,3,5])
4
>>> split(5, [5,3,1,7,2,5,5])
4
>>> split(5, [5,3,1,5,5])
2
>>> split(5, [1,3,1,1,1])
5
>>> split(5, [5,1,7,2,3,5])
4
"""


def split(x, l):
    for pos in range(len(l)):
        left, right = check(l, pos, x)
        if left == right:
            return pos
    return pos + 1


def check(l, pos, x):
    left = l[:pos].count(x)
    right = len(l) - pos - l[pos:].count(x)
    return left, right
