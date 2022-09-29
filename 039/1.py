"""
https://www.codewars.com/kata/55908aad6620c066bc00002a

Check to see if a string has the same amount of 'x's and 'o's.
The method must return a boolean and be case insensitive.
The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false


>>> count_letter("ooo",'o')
3

>>> count_letter("oo",'o')
2

>>> count_letter("oO",'o')
2

>>> count_letter("xxx",'x')
3

>>> count_letter("xxX",'x')
3

>>> XO("xxoo")
True

>>> XO("xxxoo")
False

>>> XO("XOxo")
True

>>> XO("XacbbaabailjalOxo")
True
"""


def count_letter(string, letter):
    count = 0
    for l in string.lower():
        if l == letter:
            count += 1
    return count

def XO(string):
    # return count_letter(string, "o") == count_letter(string, "x")
    string = string.lower()
    return string.count('o') == string.count('x')
