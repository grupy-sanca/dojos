"""
https://www.codewars.com/kata/56684677dc75e3de2500002b/python

A comfortable word is a word which you can type always alternating the hand you type with (assuming you type using a QWERTY keyboard and use fingers as shown in the image below).

That being said, complete the function which receives a word and returns true if it's a comfortable word and false otherwise.

The word will always be a string consisting of only ascii letters from a to z.

To avoid problems with image availability, here's the lists of letters for each hand:

    Left: q, w, e, r, t, a, s, d, f, g, z, x, c, v, b
    Right: y, u, i, o, p, h, j, k, l, n, m

Examples:

"yams"  -->  true
"test"  -->  false

>>> is_comfortable("test")
False
>>> is_comfortable("yams")
True
>>> is_comfortable("qyw")
True
>>> is_comfortable("q")
True
>>> is_comfortable("qyww")
False
>>> is_comfortable("yuiop")
False
>>> is_comfortable("qwert")
False
>>> is_comfortable("aaaaa")
False
"""


def is_comfortable(word):
    is_left = 1
    is_right = 2
    left = set(['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 
                'f', 'g', 'z', 'x', 'c', 'v', 'b'])

    previous_position = is_left if word[0] in left else is_right
    for char in word[1:]:
        current_position = is_left if char in left else is_right
        if current_position == previous_position:
            return False
        previous_position = current_position 

    return True