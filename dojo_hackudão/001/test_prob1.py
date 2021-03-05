"""
teste -> passa teste -> refatora -> teste
- passa teste ninguém fala
- teste & refatora podem falar
- fase atual: refatora
"""

import pytest

from prob1 import (
    math_repeated_string,
    multiply_string_repeated_string,
    cycle_for_mod_string,
    cycle_repeated_string,
    cycle_until,
    count,
    itercount_repetead_string,
)

@pytest.mark.parametrize('func', (
    math_repeated_string,
    multiply_string_repeated_string,
    cycle_for_mod_string,
    cycle_repeated_string,
    itercount_repetead_string,
))
def test_repeated_string(func):
    assert func("aba", 10) == 7
    assert func("abac", 10) == 5
    assert func("bxcvs", 200) == 0
    assert func("ahasgvbhjsvghjvahjsvhjvshjkvajkshvkahvahjsywe", 100000) == 13334
    assert func("abacdef", 4) == 2
    assert func("abacdaf", 2) == 1


# cycle até n (ao invés de cycle infinitamente)
def test_cycle_until():
    assert list(cycle_until("abc", 10)) == [
        "a", "b", "c", "a", "b", "c", "a", "b", "c", "a"
    ]

def test_itercount():
    assert count("a", [
        "a", "b", "c", "a", "b", "c", "a", "b", "c", "a"
    ]) == 4
    assert count("a", "abcabcabca") == 4
    assert count(17, [1, 2, 3, 17, 4, 5, 6, 17, 7, 8, 9]) == 2
    assert count("eita", ["ola", "mundo", "eita", "teste", "eita"]) == 2