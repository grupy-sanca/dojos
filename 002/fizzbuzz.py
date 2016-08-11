"""
Percorra numeros de 1 a n imprima fizz se numero é multiplo de 3,
buzz se for de 5, e fizzbuzz se for dos dois
"""


def fizzbuzz(n):
    """
    >>> fizzbuzz(3)
    fizz
    >>> fizzbuzz(5)
    fizz
    buzz
    >>> fizzbuzz(15)
    fizz
    buzz
    fizz
    fizz
    buzz
    fizz
    fizzbuzz
    >>> fizzbuzz(30)
    fizz
    buzz
    fizz
    fizz
    buzz
    fizz
    fizzbuzz
    fizz
    buzz
    fizz
    fizz
    buzz
    fizz
    fizzbuzz
    >>> fizzbuzz(45)
    fizz
    buzz
    fizz
    fizz
    buzz
    fizz
    fizzbuzz
    fizz
    buzz
    fizz
    fizz
    buzz
    fizz
    fizzbuzz
    fizz
    buzz
    fizz
    fizz
    buzz
    fizz
    fizzbuzz
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
