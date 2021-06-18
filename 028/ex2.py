"""
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name.
They are now trying out various combinations of company names and logos based on this condition.
Given a string, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

-> Print the three most common characters along with their occurrence count.
-> Sort in descending order of occurrence count.
-> If the occurrence count is the same, sort the characters in alphabetical order.

-> ordena a string inicial -> garante que o dicionário tá ordenado
-> cria outra função que roda 3 vezes, e antes do for chama letter_count_func

Example:

* input: 
aabbbccde

* output:
[("b": 3), ("a":  2), ("c": 2)]

>>> main('aaabbc')
[('a', 3), ('b', 2), ('c', 1)]

>>> main('aaabbcdef')
[('a', 3), ('b', 2), ('c', 1)]

>>> main('aaabbbcccdef')
[('a', 3), ('b', 3), ('c', 3)]

>>> main('abcccdddeffff')
[('f', 4), ('c', 3), ('d', 3)]
"""

def letter_count_func(string):
    letter_count = {}
    for letter in string:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count

def sort_values(x):
    return [-x[1], x[0]]

def main(string):
    letter_count = letter_count_func(string)
    letter_count = sorted(letter_count.items(), key=sort_values, reverse=True)
    return letter_count[-1:-4:-1]