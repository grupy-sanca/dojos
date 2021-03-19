"""
https://www.hackerrank.com/challenges/balanced-brackets/problem

>>> is_balanced("()")
'YES'
>>> is_balanced("(()")
'NO'
>>> is_balanced("(())")
'YES'
>>> is_balanced("((()")
'NO'
>>> is_balanced("[()]")
'YES'
>>> is_balanced("[[[]")
'NO'
>>> is_balanced("]]")
'NO'
>>> is_balanced("(){}[]")
'YES'
"""

brackets = {
    '(': ')',
    '{': '}',
    '[': ']',
}

def is_balanced(string):
    if len(string) % 2 == 1:
        return 'NO'
    
    pilha = []
    for c in string:
        if c in brackets:
            pilha.append(c)
        elif not pilha:
            return "NO"
        else:
            item = pilha.pop()
            if c != brackets[item]:
                return "NO"           

    if pilha:
        return "NO"
    return 'YES'
