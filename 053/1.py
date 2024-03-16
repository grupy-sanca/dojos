"""
Uma função extremamente importante na comunicação é a codificação da mensagem,
seja para economizar recursos na hora da transmissão ou para dificultar o acesso
indesejado do conteúdo (criptografia).

Vamos construir uma forma de codificar nossas mensagens:

1 - Construa uma função encode_string que receba uma frase (somente letras sem acentos e espaços)
e que retorne um valor numérico associado à cada uma das letras. A codificação precisa ser consistente,
isto é, mesmas letras devem ser codificadas para os mesmos números.

Exemplo: encode_string("DOJO") —> "1 2 3 2" é uma codificação aceitável,
pois ambos "O"s são mapeados para o mesmo número 2

>>> encode_letter("A")
1

>>> encode_letter("B")
2

>>> encode_word("DOJO")
'4 15 10 15'

>>> encode_word("DOJO PY")
'4 15 10 15 27 16 25'

>>> encode_word("dojo")
'31 42 37 42'
"""
from string import ascii_uppercase, ascii_lowercase


def encode_letter(letter: str) -> int:
    mapping = {char: number + 1 for number, char in enumerate(ascii_uppercase + " " + ascii_lowercase)}
    return mapping.get(letter)


def encode_word(word: str):
    return " ".join([str(encode_letter(letter)) for letter in word])
