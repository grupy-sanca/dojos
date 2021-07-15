from unittest import mock
import functools

from main import main
import pytest
from wallet import Wallet


@pytest.fixture
def wallet():
    return Wallet()


def test_wallet_report(wallet, capsys):
    main(["report"], wallet=wallet)

    captured = capsys.readouterr()
    assert captured.out == "Valor               Data                    Categoria               Descrição\n"


def test_wallet_add_missing_mandatory_argument(wallet, capsys):
    main(["add"], wallet=wallet)

    assert wallet.balance == 0
    assert capsys.readouterr().err == "Missing parameter\n"


def test_wallet_add(wallet, capsys):
    main(["add", "15"], wallet=wallet)

    assert wallet.balance == 15
    assert capsys.readouterr().out == ""


def test_wallet_add_twice(wallet, capsys):
    main(["add", "15"], wallet=wallet)
    main(["add", "15"], wallet=wallet)

    assert wallet.balance == 30
    assert capsys.readouterr().out == ""