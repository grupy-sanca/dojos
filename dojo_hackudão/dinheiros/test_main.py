from io import StringIO

from main import main, wallet


def test_wallet_report(capsys):
    main(["report"])

    captured = capsys.readouterr()
    assert captured.out == "Valor               Data                    Categoria               Descrição\n"


def test_wallet_add_missing_mandatory_argument(capsys):
    main(["add"])

    assert wallet.balance == 0
    assert capsys.readouterr().err == "Missing parameter\n"


def test_wallet_add(capsys):
    main(["add", "15"])

    assert wallet.balance == 15
    assert capsys.readouterr().out == ""