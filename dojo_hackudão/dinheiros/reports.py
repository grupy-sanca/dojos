"""
Relatórios da carteira printado na telas

- Resumo / Summary
    - Por mês
    - Total
    - Categorias
    - Filtros?

- Transações
    - Tudão
    - Ordenação?
    - Filtros:
        - Data / range
        - Categoria
        - Descrição
        - Valor / range

DONE:
- Transações
    - Tudão
"""

from datetime import datetime

HEADERS = ("Valor", "Data", "Categoria", "Descrição")


def truncate(string, num_chars):
    if len(string) > num_chars:
        return string[:num_chars - 3] + "..."
    return string


def generate_transaction_text_report(wallet):
    line = "{value:<20}{timestamp:<24}{category:<24}{description}"
    report = "{:<20}{:<24}{:<24}{}".format(*HEADERS)
    for transaction in wallet._transactions:
        report += "\n"
        report += line.format(
            value=str(transaction.value),
            timestamp=transaction.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            category=truncate(transaction.category, 23),
            description=truncate(transaction.description, 23),
        )

    return report