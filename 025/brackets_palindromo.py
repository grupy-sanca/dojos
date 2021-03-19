"""
https://www.hackerrank.com/challenges/balanced-brackets/problem

>>> is_balanced("()")
'YES'
>>> is_balanced("([)")
'NO'
>>> is_balanced("{([])}")
'YES'
"""

closing_brackets = {
    '(': ')',
    '{': '}',
    '[': ']',
}

def is_balanced(string):
    if len(string) % 2 != 0:
        return 'NO'

    meio = len(string) // 2
    for i in range(1, meio):
        start = string[i - 1]
        end = string[-i]
        if end != closing_brackets[start]:
            return 'NO'

    return 'YES'
