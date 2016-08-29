r"""
In recreational mathematics, a magic square is an arrangement of distinct numbers
(i.e., each number is used once), usually integers, in a square grid, where
the numbers in each row, and in each column, and the numbers in the main
and secondary diagonals, all add up to the same number, called the "magic constant."

For example:
    4    9    2 -> 15
    3    5    7 -> 15
    8    1    6 -> 15
   /v    v    v \
 15 15   15   15  15

In this problem you will have to create a function that receives a 'square' and
returns True if it is magic and False otherwise.

For example, the above square will be passed like: [4, 9, 2, 3, 5, 7, 8, 1, 6]
and the output should be True

[9, 4, 7, 3, 5, 2, 8, 6, 1] should return False

This problem was created by the members of grupy-sanca and has been submitted
to codewars, check it out:
    https://www.codewars.com/kata/magic-square-validator/
"""


def check_lines(square):
    """
    >>> square = [4, 9, 2, 3, 5, 7, 8, 1, 6]
    >>> ex_square = [4, 9, 2, 3, 5, 7, 8, 6, 1]
    >>> check_lines(square)
    True
    >>> check_lines(ex_square)
    True
    >>> check_lines(range(1, 10))
    False
    """
    line1 = sum(square[0:3]) == 15
    line2 = sum(square[3:6]) == 15
    line3 = sum(square[6:9]) == 15
    return line1 and line2 and line3


def check_columns(square):
    """
    >>> square = [4, 9, 2, 3, 5, 7, 8, 1, 6]
    >>> ex_square = [4, 9, 2, 3, 5, 7, 8, 6, 1]
    >>> check_columns(range(1, 10))
    False
    >>> check_columns(ex_square)
    False
    >>> check_columns(square)
    True
    """
    col1 = square[0] + square[3] + square[6] == 15
    col2 = square[1] + square[4] + square[7] == 15
    col3 = square[2] + square[5] + square[8] == 15
    return col1 and col2 and col3


def check_diagonals(square):
    """
    >>> square = [4, 9, 2, 3, 5, 7, 8, 1, 6]
    >>> ex_square = [4, 9, 2, 3, 5, 7, 8, 6, 1]
    >>> check_diagonals(square)
    True
    >>> check_diagonals(ex_square)
    False
    """
    dia1 = square[0] + square[4] + square[8] == 15
    dia2 = square[2] + square[4] + square[6] == 15
    return dia1 and dia2


# def is_magical(square):
#     """
#     >>> square = [4, 9, 2, 3, 5, 7, 8, 1, 6]
#     >>> ex_square = [4, 9, 2, 3, 5, 7, 8, 6, 1]
#     >>> is_magical(square)
#     True
#     >>> is_magical(ex_square)
#     False
#     >>> is_magical([9, 4, 7, 3, 5, 2, 8, 6, 1])
#     False
#     >>> is_magical(range(1, 10))
#     False
#     """
#     return check_lines(square) and check_columns(square) and check_diagonals(square)


def is_magical(sq):
    """
    >>> square = [4, 9, 2, 3, 5, 7, 8, 1, 6]
    >>> ex_square = [4, 9, 2, 3, 5, 7, 8, 6, 1]
    >>> is_magical(square)
    True
    >>> is_magical(ex_square)
    False
    >>> is_magical([9, 4, 7, 3, 5, 2, 8, 6, 1])
    False
    >>> is_magical(range(1, 10))
    False
    >>> is_magical([8, 1, 6, 3, 5, 7, 4, 9, 2])
    True
    """
    valid_lines = sum(sq[0:3]) == 15 and sum(sq[3:6]) == 15 and sum(sq[6:9]) == 15
    valid_columns = (sq[0] + sq[3] + sq[6] == 15
                     and sq[1] + sq[4] + sq[7] == 15
                     and sq[2] + sq[5] + sq[8] == 15)
    valid_diagonals = sq[0] + sq[4] + sq[8] == 15 and sq[2] + sq[4] + sq[6] == 15
    return valid_lines and valid_columns and valid_diagonals
