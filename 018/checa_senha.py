"""
Checador de senhas -> https://www.codewars.com/kumite/5b748f34b1181438060005ae
1) password must be no less than 8 characters long
2) password must have at least 1 capital letter
3) password must have at least 1 number
4) password must have at least 1 special character
for this Kata special characters are considered:
     ( ! " # $ % & ' ( ) * + ' - . / ; : < > = or ?)

>>> checa_senha("abc")
False
>>> checa_tamanho("abcdefgh")
True
>>> checa_tamanho("ab")
False
>>> checa_maiusculo("abc")
False
>>> checa_maiusculo("A")
True
>>> checa_maiusculo("aBBsaasfaaAAAA")
True
>>> checa_maiusculo("123")
False
>>> checa_numero("abc1")
True
>>> checa_numero("abcde")
False
>>> checa_maiusculo('!@$#$saddfg789')
False
>>> checa_caracter('#')
True
>>> checa_caracter("abc")
False
>>> checa_senha("#abCd12345")
True
>>> checa_senha('A123456789')
False
>>> checa_senha('carambadeteclado')
False
>>> checa_senha('123321')
False
>>> checa_senha(':@')
False
>>> checa_senha('PO')
False
>>> checa_senha('~ÃÇÀAnnnn1')
False
"""
import string


def checa_senha(senha):
    return (
        checa_tamanho(senha) and
        checa_caracter(senha) and
        checa_numero(senha) and
        checa_maiusculo(senha)
    )

def checa_tamanho(senha):
    return len(senha) >= 8

def checa_maiusculo(senha):
    for letra in senha:
        if letra in string.ascii_uppercase:
            return True
    return False

def checa_numero(senha):
    for letra in senha:
        if letra.isnumeric():
            return True
    return False

def checa_caracter(senha):
    especial = """!"#$%&'()*+'-./;:<>=?"""
    for letra in senha:
        if letra in especial:
            return True
    return False
