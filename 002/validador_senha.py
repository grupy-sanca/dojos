"""
Análise de Senha (fraca, média, forte). Seguir algum critério oficial?
Fraca:
Média:8+ caracteres, letras e números
Forte:8+ caracteres, letras maiúsculas e minúsculas,
números e caracteres especiais
"""


def possui_caixa_alta_e_baixa(string):
    """
    >>> possui_caixa_alta_e_baixa("abc")
    False
    >>> possui_caixa_alta_e_baixa("ABC")
    False
    >>> possui_caixa_alta_e_baixa("123")
    False
    >>> possui_caixa_alta_e_baixa("AbCdEf123!_2")
    True
    """

    possui_caixa_baixa = False
    possui_caixa_alta = False

    for char in string:
        if char.isupper():
            possui_caixa_alta = True
        elif char.islower():
            possui_caixa_baixa = True

    return possui_caixa_alta and possui_caixa_baixa


def possui_caracter_especial(string):
    """
    >>> possui_caracter_especial("aaa")
    False
    >>> possui_caracter_especial("123")
    False
    >>> possui_caracter_especial("aaa123")
    False
    >>> possui_caracter_especial("1aaa!")
    True
    """

    for char in string:
        if not char.isalnum():
            return True
    return False


def possui_letra_e_numero(string):
    """
    >>> possui_letra_e_numero('Abc')
    False
    >>> possui_letra_e_numero('Abc123')
    True
    >>> possui_letra_e_numero('12345')
    False
    """
    possui_digito = False
    possui_letra = False
    for char in string:
        if char.isdigit():
            possui_digito = True
        if char.isalpha():
            possui_letra = True

    return possui_digito and possui_letra


def eh_fraca(senha):
    """
    >>> eh_fraca("Senhamedia123")
    False
    >>> eh_fraca("Senhaforte123!")
    False
    >>> eh_fraca("123123213123")
    True
    >>> eh_fraca("senhafortinha")
    True
    >>> eh_fraca("senhafortinha!")
    True
    >>> eh_fraca("123")
    True
    >>> eh_fraca("qwerty!")
    True
    """
    return not eh_media(senha) and not eh_forte(senha)


def eh_media(senha):
    """
    >>> eh_media("senha")
    False
    >>> eh_media("senhamedia")
    False
    >>> eh_media("senhamedia123")
    True
    >>> eh_media("12345678")
    False
    >>> eh_media("Senhamedia123")
    True
    >>> eh_media("Senhamedia123!")
    False
    """
    if eh_forte(senha):
        return False

    if len(senha) < 8:
        return False

    return possui_letra_e_numero(senha)


def eh_forte(string):
    """
    >>> eh_forte("aaa123")
    False
    >>> eh_forte("senhaforte")
    False
    >>> eh_forte("12345678")
    False
    >>> eh_forte("senhaforte123")
    False
    >>> eh_forte("senhaforte123!")
    False
    >>> eh_forte("Senhaforte123!")
    True
    """

    if len(string) < 8:
        return False

    if not possui_letra_e_numero(string):
        return False

    if not possui_caracter_especial(string):
        return False

    if not possui_caixa_alta_e_baixa(string):
        return False

    return True
