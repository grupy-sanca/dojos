"""
Seguradora que vende seguro-viagem e quer expandir o negócio para oferecer o serviço
para outros países, então o sistema que já existe hoje e possui uma classe que representa
real precisa suportar outras moedas para conseguir calcular quantos reais é necessário pagar
para ocorrências gastas em outra moeda.

          grupal            duplal           grupal        grupal
# TDD: definir teste -> faz teste passar -> refatora -> definir teste

TODO:
- O que tem hoje (e vamos ter que reimplementar)
    - Real

- Múltiplas moedas (dólar, real etc.)
    - Conversão
    - Somar
    - Subtrair
    - Multiplicar


- Pensar em operações com tipos inválidos
- Valores inválidos (negativo)?

DOING:
- Real

DONE:
- Real
    - Comparação
        - Igual / Diferente
        - Maior
    - Subtração
    - Soma
    - Multiplicação por escalar
    - Divisão por escalar
    - Usar sobrecarga de operadores

- Comparação com functools.total_ordering (implementa __eq__ e __lt__)
    - Maior ou igual
    - Menor
    - Menor ou igual

"""

import functools
from numbers import Number

import pytest


class MoneyCrazy:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        other_cls = type(other)
        return other_cls(self.value + other.value)
        #return type(other)(self.value + other.value)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.value += other.value
        return self


def test_money_crazy():
    assert Real(5) + MoneyCrazy(10) == Real(15)
    assert MoneyCrazy(10) + Real(5) == Real(15)

    dinheiro = MoneyCrazy(10)
    dinheiro += MoneyCrazy(5)
    assert dinheiro.value == MoneyCrazy(15).value


@functools.total_ordering
class Real:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __sub__(self, other): 
        return Real(self.value - other.value)

    def __add__(self, other):  # other: Dollar
        if isinstance(other, Real):
            return Real(self.value + other.value)
        
        return NotImplemented

    def __mul__(self, scalar):
        if not isinstance(scalar, Number):
            raise TypeError("pow mano passa um numero")

        return Real(self.value * scalar)

    def __truediv__(self, scalar):
        return Real(self.value / scalar)

    def __neg__(self):
        return Real(-self.value)
    
    def __str__(self):
        value = float(self.value)
        return f"R$ {value:.2f}".replace('.', ',')

    def __repr__(self):
        return f"Real({self.value})"


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