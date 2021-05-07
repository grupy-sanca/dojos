"""
Aplicação de gestão de gastos pessoais, que permite cadastrar os gastos e receitas, com suporte
a "contas" diferentes, categorias de gastos e com uma série de relatórios úteis.

                   Ciclo TDD
    _________________________________________
    |                   |                   |
    grupal            duplal           grupal       grupal

definir teste -> faz teste passar -> refatora -> definir teste
"""

import functools
from numbers import Number

import pytest


@functools.total_ordering
class Real:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == Real(other).value

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