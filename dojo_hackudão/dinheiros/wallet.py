"""
                   Ciclo TDD
    _________________________________________
    |                   |                   |
    grupal            duplal           grupal       grupal

definir teste -> faz teste passar -> refatora -> definir teste

Aplicação de Caretira:
    - Transação
        - Valor
        - Timestamp pago
        - Categoria: str
        - Descrição
        - Se é gasto ou recebimento
    - Carteira (Planilha do Excel)
        - Nome / identificador
        - Linhas
        - Saldo
        * balanço do mês / período
        * resumo atual / por categoria

TODO:
- Carteira
    - Balanço do mês
    - Resumo atual
    - "Relatórios"
- Conta bancária
- Transação
    - Usar enum

DOING:

DONE:
- Transação
    - Validação de dados
        - Tratar transação com 0
"""

from dataclasses import dataclass
from datetime import datetime
from unittest import mock

import pytest

from real import Real


@dataclass
class Transaction:
    DEFAULT_CATEGORY = "Default"
    IN = "IN"
    OUT = "OUT"

    value: float
    timestamp: datetime = None
    category: str = DEFAULT_CATEGORY
    description: str = ""

    def __post_init__(self):
        if self.value == 0:
            raise ValueError

        self.timestamp = self.timestamp or datetime.now()
        
    @property
    def type(self):
        if self.value > 0:
            return Transaction.IN
        return Transaction.OUT


def test_transaction():
    transaction = Transaction(
        value=-10,
        timestamp=datetime(2021, 5, 5, 10),
        category="comida",
        description="almoço delícia",
    )

    assert transaction.value == Real(-10)
    assert transaction.timestamp == datetime(2021, 5, 5, 10)
    assert transaction.category == "comida"
    assert transaction.description == "almoço delícia"
    assert transaction.type == Transaction.OUT


def test_transaction_default():
    transaction = Transaction(
        value=5.55,
        timestamp=datetime(2021, 5, 5, 10),
    )

    assert transaction.category == Transaction.DEFAULT_CATEGORY
    assert transaction.description == ""
    assert transaction.type == Transaction.IN


@pytest.mark.freeze_time
def test_transaction_timestamp_default():
    transaction = Transaction(value=10.10)
    
    assert transaction.timestamp == datetime.now()


def test_transaction_value_zero():
    with pytest.raises(ValueError):
        transaction = Transaction(value=0)