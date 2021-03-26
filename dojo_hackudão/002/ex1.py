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
        - Soma
        - Multiplicação por escalar
        - Divisão por escalar

        - Comparação
            - Maior ou igual
            - Menor
            - Menor ou igual

- Múltiplas moedas (dólar, real etc.)
    - Conversão
    - Somar
    - Subtrair
    - Multiplicar

- Usar sobrecarga de operadores
- Pensar em operações com tipos inválidos
- Valores inválidos (negativo)?

DOING:
- Real
    - Subtração


DONE:
- Real
        - Comparação
            - Igual / Diferente
            - Maior



"""
import pytest


class Real:
    def __init__(self, value):
        self.value = value

    def equals(self, other):
        return self.value == other.value

    def greater(self, other):
        return self.value > other.value

    def minus(self, other):
        return Real(self.value - other.value)


@pytest.mark.parametrize("other_value,result", [
    (Real(5), True),
    (Real(5.1), False),
    (Real(10), False),
    (Real(2 ** 32), False),
    (Real(10_000_000_000), False),
])
def test_real_is_equals_five(other_value, result):
    assert Real(5).equals(other_value) is result

@pytest.mark.parametrize("other_value,result", [
    (Real(50), False),
    (Real(50.1), False),
    (Real(4.999999), True),
    (Real(0), True),
    (Real(10_000_000_000), False),
])
def test_real_is_greater_than_five(other_value, result):
    assert Real(5).greater(other_value) is result


def test_five_minus_other_value():
    result = Real(5).minus(Real(3))

    assert result.equals(Real(2))


def test_five_minus_other_value_negative():
    result = Real(3).minus(Real(5))

    assert result.equals(Real(-2))