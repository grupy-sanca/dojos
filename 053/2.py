"""
2 - Precisamos agora conseguir ler mensagens codificadas enviadas para nós.
Crie uma função decode_string que receba uma string contendo números e espaços
e retorne a mensagem original enviada, transformando cada número em sua letra correspondente.

Atente-se para mensagens com mais de uma palavra, pois elas devem ser decodificadas corretamente.

Exemplo: decode_string("1 2 3 2  4 5 6 7 2 8") --> "DOJO PYTHON"

>>> decode_letter('1')
'A'

>>> decode_letter('2')
'B'

>>> decode_word('4 15 10 15')
'DOJO'

>>> decode_word('4 15 10 15 27 16 25')
'DOJO PY'

"""
from string import ascii_uppercase, ascii_lowercase


def decode_letter(num: str) -> str:
    mapping = {str(number + 1): char for number, char in enumerate(ascii_uppercase + " " + ascii_lowercase)}
    return mapping.get(num)


def decode_word(number_str: str) -> str:
    _list = number_str.split(' ')
    return ''.join(decode_letter(number) for number in _list)
