import pickle

from wallet import Wallet


def get_wallet():
    try:
        with open("wallet.bin", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return Wallet()


def save_wallet(wallet):
    with open("wallet.bin", "wb") as f:
        pickle.dump(wallet, f)