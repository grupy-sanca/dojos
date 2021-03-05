"""
https://www.hackerrank.com/challenges/repeated-string/problem

Sample Input
aba
10

abaabaabaa  | tamanho 10

-> abaabaabaa|baabaabaabaabaaba...
-> abaabaabaa -> 7 a's
Sample Output
7
"""

# max(s) == 100, max(s) == 10e12

def multiply_string_repeated_string(s, n):
    # intuitivo
    infinite_string = s * n  # O(s * n) memória / O(n) tempo
    return infinite_string[:n].count('a')


def math_repeated_string(s, n):
    # resolver matematicamente  O(s) / O(s)
    number_of_a_in_original = s.count('a')
    repetitions = n // len(s)
    remaining_string_position = n % len(s)
    number_of_a_in_remaining = s[:remaining_string_position].count('a')

    return number_of_a_in_original * repetitions + number_of_a_in_remaining


def cycle_for_mod_string(s, n):
    # O(s) / O(n)
    count_a = 0 

    for i in range(n):  # tentar usar cycle depois generator
        if s[i % len(s)] == 'a':
            count_a += 1
        
    return count_a


import itertools

def cycle_repeated_string(s, n):
    # O(s) / O(n)
    count_a = 0
    for char in cycle_until(s, n):  # cycle_until gera a string q precisamos
        if char == 'a':
            count_a += 1
    return count_a


def cycle_until(s, n):
    i = 0
    for char in cycle(s):  # loop infinito
        yield char
        i += 1
        if i == n:
            return


def cycle(s):
    while True:
        for c in s:
            yield c


def count(query, iterator):
    count = 0
    for item in iterator:
        if item == query:
            count = count + 1

    return count


def itercount_repetead_string(s, n):
    # pegou a multiply (função debaixo) e acabou com o problema
    # de memória usando geradores / itertools
    infinite_string = itertools.cycle(s)
    substring = itertools.islice(infinite_string, n)
    return count("a", substring)


def multiply_string_repeated_string(s, n):
    # intuitivo
    infinite_string = s * n  # O(s * n) memória / O(n) tempo
    substring = infinite_string[:n]
    return substring.count('a')