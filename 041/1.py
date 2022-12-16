"""
https://www.codewars.com/kata/633b8be2b5203f003011d79e

Sami is practicing her aim with her bow and is shooting some balloons in the air.
On each balloon, they have different numbers written on them which represent their size.
She would like to pop the balloon highest in the air that also has the most balloons of the
same size present. If there is a tie, then she will instead pop the balloon of the size
highest in the air. Do you think you can output which balloon she pops on each shot?

You will be provided an array of the balloons as integers (the integers representing the sizes)
in lowest to highest order in the air. You will also be given an integer pops, which will be the
number of pops that Sami will execute.

Example

pops = 4
balloons = [5, 7, 5, 7, 4, 5]

pop #1: 5
pop #2: 7
pop #3: 5
pop #4: 4

return: [5, 7, 5, 4]

>>> count_repetition([5, 7, 5, 7, 4, 5])
{1: [4], 3: [5], 2: [7]}

>>> count_repetition([5, 7, 5, 7])
{2: [5, 7]}

>>> count_repetition([5, 7, 4])
{1: [4, 5, 7]}

>>> find_pop_value([5, 7, 5, 7, 4, 5])
5

>>> find_pop_value([5, 7, 5, 7])
7

>>> find_pop_value([5, 7, 5, 5, 7])
5

>>> pop_one([5, 7, 5, 7, 4, 5], 5)
[5, 7, 5, 7, 4]

>>> pop_one([5, 7, 5, 7, 4], 7)
[5, 7, 5, 4]

>>> pop_n([5, 7, 5, 7, 4, 5], 4)
[5, 7, 5, 4]

>>> pop_n([5, 7, 5, 7, 4, 5], 6)
[5, 7, 5, 4, 7, 5]

>>> pop_n([1, 1, 1, 1], 2)
[1, 1]

>>> pop_n([1, 1, 1, 1], 0)
[]
"""

def pop_n(numbers, n):
    result = []
    for i in range(n):
        pop_value = find_pop_value(numbers)
        result.append(pop_value)
        numbers = pop_one(numbers, pop_value)
    return result

def pop_one(numbers, pop_value):
    numbers_reversed = numbers[::-1]
    numbers_reversed.remove(pop_value)

    return numbers_reversed[::-1]


def find_pop_value(numbers):
    counted = count_repetition(numbers)
    larger = sorted(counted.keys())[-1]
    lista = counted[larger]

    for number in numbers[::-1]:
        if number in lista:
            return number


def count_repetition(numbers):
    set_number = set(numbers)
    count = {}
    for number in set_number:
        l = count.get(numbers.count(number), [])
        l.append(number)
        count[numbers.count(number)] = l
    return count
