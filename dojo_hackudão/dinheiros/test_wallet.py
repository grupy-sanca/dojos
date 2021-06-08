from datetime import datetime

import pytest

from real import Real
from wallet import Transaction, Wallet


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


def test_wallet():
    wallet = Wallet(name="name")

    assert wallet.name == "name"
    assert wallet.balance == Real(0)


def test_wallet_transaction():
    transaction1 = Transaction(value=5)
    transaction2 = Transaction(value=10)

    wallet = Wallet(
        name="name",
        _transactions=[transaction1, transaction2]
    )

    assert wallet.balance == Real(15)
    assert len(wallet._transactions) == 2


def test_wallet_default_balance():
    wallet = Wallet(name="name")
    assert wallet.balance == Real(0)


def test_add_new_transaction():
    wallet = Wallet(name="name")
    wallet._add_transaction(Transaction(value=15))
    assert wallet.balance == Real(15)


@pytest.mark.freeze_time
def test_wallet_summary():
    wallet = Wallet(name="name", _transactions=[Transaction(value=10), Transaction(value=10)])
    
    assert wallet.summary() == {
        "name": "name",
        "transactions": [Transaction(value=10), Transaction(value=10)],
        "balance": Real(20),
        "timestamp": datetime.now(),
    }


def test_wallet_summary_date_interval():
    transaction1 = Transaction(value=-10, timestamp=datetime(2021, 5, 5))
    transaction2 = Transaction(value=-10, timestamp=datetime(2021, 5, 10))
    transaction3 = Transaction(value=-10, timestamp=datetime(2020, 5, 10))

    wallet = Wallet(name="name", _transactions=[transaction1, transaction2, transaction3])

    # assert wallet.summary_with_interval(datetime(2021), datetime(2021))


def test_wallet_add():
    wallet = Wallet(name="name")
    wallet.add(value=15)
    assert wallet.balance == Real(15)


def test_wallet_withdraw():
    wallet = Wallet(name="wallet")
    wallet.withdraw(value=10)
    assert wallet.balance == Real(-10)


def test_wallet_add_with_category_and_description():
    wallet = Wallet(name="name")
    wallet.add(value=15, category="test_category", description="test_description", timestamp=datetime(2020, 10, 10, 20))

    assert wallet._transactions[0].category == "test_category"
    assert wallet._transactions[0].description == "test_description"
    assert wallet._transactions[0].timestamp == datetime(2020, 10, 10, 20)


def test_wallet_withdraw_with_category_and_description():
    wallet = Wallet(name="name")
    wallet.withdraw(value=15, category="test_category", description="test_description", timestamp=datetime(2020, 10, 10, 20))

    assert wallet._transactions[0].category == "test_category"
    assert wallet._transactions[0].description == "test_description"
    assert wallet._transactions[0].timestamp == datetime(2020, 10, 10, 20)