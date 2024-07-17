"""
Cifra de César

Implemente a cifra de César, um tipo simples de criptografia onde cada letra do texto é
deslocada um número fixo de posições no alfabeto. Escreva funções para criptografar e
descriptografar mensagens usando a cifra de César. A função de criptografia deve aceitar
uma string de texto claro e um número de deslocamento, e a função de descriptografia deve
aceitar uma string criptografada e o mesmo número de deslocamento para recuperar o texto claro.

Ambos os textos só podem ter letras sem acentos.

Exemplo:
cifra("HELLO", 3)
'KHOOR'

decifra("KHOOR", 3)
'HELLO'

>>> cifra_letra("A", 1)
'B'

>>> cifra_letra("B", 1)
'C'

>>> cifra_letra("Z", 1)
'A'

>>> cifra_letra("A", 2)
'C'

>>> cifra("HELLO", 3)
'KHOOR'

>>> cifra("HELL", 3)
'KHOO'

>>> cifra("A", 3)
'D'

>>> cifra("A", 26*10 + 1)
'B'

>>> cifra_letra("B", -1)
'A'

>>> cifra_letra("A", -1)
'Z'

>>> decifra("KHOOR", 3)
'HELLO'

>>> decifra("KHOO", 3)
'HELL'

"""

from string import ascii_uppercase


def cifra_letra(letra, rotacao):
    index = ascii_uppercase.find(letra)
    return ascii_uppercase[(index + rotacao) % len(ascii_uppercase)]


def cifra(frase, rotacao):
    return ''.join([cifra_letra(letra, rotacao) for letra in frase])


def decifra(frase, rotacao):
    return cifra(frase, -rotacao)
