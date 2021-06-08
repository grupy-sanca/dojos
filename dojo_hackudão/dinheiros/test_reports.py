from datetime import datetime
from pytest import fixture
from wallet import Wallet

from reports import generate_transaction_text_report


@fixture
def wallet():
    return Wallet(name="name")


def test_transaction_report(wallet):
    wallet.add(value=3000, category="Salário", description="Caiu o pagode", timestamp=datetime(2021, 5, 5, 8))
    wallet.withdraw(value=100, category="Comida e Alimentação", description="Pizza muito boa essa pizza", timestamp=datetime(2021, 5, 5, 20))
    wallet.withdraw(value=1000, category="Casa", description="Aluguel caro", timestamp=datetime(2021, 5, 10, 10))
    wallet.withdraw(value=500, category="Casa", description="Condomínio", timestamp=datetime(2021, 5, 10, 10))
    text_report = generate_transaction_text_report(wallet)

    assert text_report == """
Valor               Data                    Categoria               Descrição
+ R$3000,00         2021-05-05 08:00:00     Salário                 Caiu o pagode
- R$100,00          2021-05-05 20:00:00     Comida e Alimentação    Pizza muito boa essa...
- R$1000,00         2021-05-10 10:00:00     Casa                    Aluguel caro
- R$500,00          2021-05-10 10:00:00     Casa                    Condomínio""".strip()


def test_transaction_report_truncate(wallet):
    wallet.withdraw(
        value=100,
        category="Eventos de Python Muito Loucos",
        description="Tem quentão e paçoquinha e pythonistas contando pyadas ruins :)",
        timestamp=datetime(2021, 5, 5, 20),
    )
    text_report = generate_transaction_text_report(wallet)
    assert text_report == """
Valor               Data                    Categoria               Descrição
- R$100,00          2021-05-05 20:00:00     Eventos de Python Mu... Tem quentão e paçoqu...""".strip()