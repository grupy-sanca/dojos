"""
    $ wallet report
    $ wallet report:monthly 2021-04
    $ wallet report:yearly 2020 --csv
    $ wallet withdraw 150 --category Comida --description Lancho diliça
    $ wallet add 3000 --category Salário
    $ wallet summary
"""
from decimal import Decimal
import sys

from reports import generate_transaction_text_report
from wallet import Wallet

# TODO persistir com pickle
wallet = Wallet("Dinheiros")


def main(argv):
    command, *args = argv

    if command == "report":
        report = generate_transaction_text_report(wallet)
        print(report)
    elif command == "add":
        if len(args) == 0:
            print("Missing parameter", file=sys.stderr)
            return
        value = Decimal(args[0])
        wallet.add(value)
        return


if __name__ == "__main__":
    main(sys.argv[1:])