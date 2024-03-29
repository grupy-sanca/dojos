"""
https://www.codewars.com/kata/5926624c9b424d10390000bf


Write a func named SumEvenFibonacci that takes a parameter of type int and returns a value of type int

Generate all of the Fibonacci numbers starting with 1 and 2 and ending on the highest number before exceeding the parameter's value

Each new number in the Fibonacci sequence is generated by adding the previous two numbers - by starting with 1 and 2(the input could be smaller), the first 10 numbers will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Sum all of the even numbers you generate and return that int

Example:
    sumEvenFibonacci(8) // returns 10 by adding the even values 2 and 8

>>> sequencia_par([1, 2, 3, 4])
[2, 4]

>>> sequencia_par([1, 2, 3, 4, 6])
[2, 4, 6]

>>> sequencia_par([1, 3])
[]

>>> fibonacci(4)
[1, 2, 3]

>>> fibonacci(6)
[1, 2, 3, 5]

>>> fibonacci(89)
[1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

>>> sum(sequencia_par(fibonacci(8)))
10

>>> sum_even_fibonacci(8)
10

"""

def sum_even_fibonacci(maximo):
    lista = fibonacci(maximo)
    return sum(sequencia_par(lista))

def sequencia_par(sequencia):
    return [n for n in sequencia if n % 2 == 0]

def fibonacci(maximo):
    if maximo == 1:
        return [1]
    if maximo == 2:
        return [1, 2]

    lista = [1, 2]
    while lista[-1] <= maximo:
        lista.append(lista[-1] + lista[-2])
    if lista[-1] > maximo:
        lista.pop()

    return lista