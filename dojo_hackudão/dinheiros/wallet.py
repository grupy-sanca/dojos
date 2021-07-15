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
- Conta bancária
- Transação
    - Usar enum

DOING:
- Carteira
    > Adicionar novas transações
    > Resumo atual
    - Balanço do mês
    - "Relatórios"

DONE:
- Transação
    - Validação de dados
        - Tratar transação com 0
"""

from dataclasses import dataclass
from datetime import datetime
from unittest import mock
from typing import List

import pytest

from real import Real


@dataclass
class Transaction:
    DEFAULT_CATEGORY = "Default"
    IN = "IN"
    OUT = "OUT"

    value: Real
    timestamp: datetime = None
    category: str = DEFAULT_CATEGORY
    description: str = ""
        
    @property
    def type(self):
        if self.value > 0:
            return Transaction.IN
        return Transaction.OUT

    def __post_init__(self):
        if self.value == 0:
            raise ValueError

        self.value = Real(self.value)
        self.timestamp = self.timestamp or datetime.now()


@dataclass
class Wallet:
    name: str = "wallet"
    _transactions: List[Transaction] = None

    @property
    def balance(self):
        return sum(transaction.value for transaction in self._transactions)

    def __post_init__(self):
        if self._transactions is None:
            self._transactions = []

    def add(self, value, category=Transaction.DEFAULT_CATEGORY, description="", timestamp=None):
        transaction = Transaction(value=value, category=category, description=description, timestamp=timestamp)
        self._add_transaction(transaction)

    def withdraw(self, value, category=Transaction.DEFAULT_CATEGORY, description="", timestamp=None):
        transaction = Transaction(value=-value, category=category, description=description, timestamp=timestamp)
        self._add_transaction(transaction)

    def _add_transaction(self, transaction):
        self._transactions.append(transaction)

    def summary(self):
        return {
            "name": self.name,
            "transactions": self._transactions,
            "balance": self.balance,
            "timestamp": datetime.now(),
        }