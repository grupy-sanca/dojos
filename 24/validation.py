"""
https://coderbyte.com/editor/Codeland%20Username%20Validation:Python3

Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string 
is a valid username according to the following rules:

1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.

If the username is valid then your program should return the True, otherwise return the string False.

>>> verifica_tamanho('straa')
True

>>> verifica_tamanho('str')
False

>>> verifica_tamanho('123456789123456789123456789')
False

>>> verifica_começo('teste')
True

>>> verifica_começo('4louu')
False

>>> verifica_chars('aaaa')
True

>>> verifica_chars('aaaa@')
False

>>> verifica_chars('aaa_a')
True

>>> verifica_chars('aaaaa23_a')
True

>>> verifica_ultimo_char('teste_1')
True

>>> verifica_ultimo_char('erro1_')
False

>>> verifica_chars('aa@aa')
False

>>> verifica_chars('aa@aa ')
False

>>> verifica_começo(' aaa')
False

>>> verifica_chars('a aa')
False

>>> verifica_username('a aa')
False

>>> verifica_username('aaaa')
True

>>> verifica_username('a123_o')
True
""" 


def verifica_tamanho(valor):
    return 4 <= len(valor) <= 25


def verifica_começo(valor):
   return valor[0].isalpha()

def verifica_chars(valor):
    resultado = True
    for letra in valor:
        if not (letra.isalnum() or letra == '_'):
            resultado = False
            break
    return resultado

def verifica_ultimo_char(valor):
    return valor[-1] != '_'

def verifica_username(valor):
    return verifica_tamanho(valor) and verifica_começo(valor) and verifica_chars(valor) and verifica_ultimo_char(valor)