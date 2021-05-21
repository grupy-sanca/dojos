import pytest

from real import Real

@pytest.mark.parametrize("other_value,result", [
    (Real(5), True),
    (Real(5.1), False),
    (Real(10), False),
    (Real(2 ** 32), False),
    (Real(10_000_000_000), False),
])
def test_real_is_equals_five(other_value, result):
    assert (Real(5) == other_value) is result


@pytest.mark.parametrize("other_value,result", [
    (Real(50), True),
    (Real(50.1), True),
    (Real(4.999999), False),
    (Real(0), False),
    (Real(10_000_000_000), True),
])
def test_real_is_lesser_than_five(other_value, result):
    assert (Real(5) < other_value) is result


def test_real_total_ordering():
    assert Real(5) > Real(0)
    assert Real(10) >= Real(10)
    assert Real(150) <= Real(200)


def test_five_minus_other_value():
    result = Real(5) - (Real(3))

    assert result == Real(2)


def test_five_minus_other_value_negative():
    result = Real(3) - (Real(5))

    assert result == Real(-2)


def test_five_plus_ten():
    result = Real(5) + (Real(10))

    assert result == Real(15)


def test_minus_five_plus_ten():
    result = Real(-5) + (Real(10))

    assert result == Real(5)


def test_five_mult_one():
    result = Real(5) * 2

    assert result == Real(10)


def test_mult_invalid_type_argument():
    with pytest.raises(TypeError):
        Real(5) * Real(5)


def test_mult_with_complex():
    assert Real(5) * (2+2j) == Real(10+10j)


def test_real_representation():
    assert str(Real(5)) == "R$ 5,00"
    assert str(Real(3.14)) == "R$ 3,14"
    assert str(Real(3.1415)) == "R$ 3,14"


def test_real_representation():
    assert repr(Real(5)) == "Real(5)"


def test_five_div_five():
    result = Real(5) / 5
    assert result == Real(1)


def test_real_negative():
    assert -Real(5) == Real(-5)