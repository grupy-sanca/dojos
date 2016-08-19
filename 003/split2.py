"""
>>> l = [1,5,1,1,1]
>>> countx(5, l)
(1, 4)
>>> split(5, l)
4
>>> split(5, [5,5,1,2,3,4,5])
4
>>> split(5, [5,5,1,2,3,4,5])
4
>>> split(5, [1,1,1,2,3,4,1])
7
>>> split(5, [5,5,1,7,2,3,5])
4
>>> split(5, [5,3,1,7,2,5,5])
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


def countx(x, l):
    count = l.count(x)
    return count, len(l) - count


def split(x, l):
    curleft = 0
    left, right = countx(x, l)
    curright = right
    for i in range(len(l)):
        if l[i] == x:
            curleft += 1
        else:
            curright -= 1
        if curleft == curright:
            return i + 1
    return len(l)
