def eh_primo(num):
    """
    >>> eh_primo(1)
    False
    >>> eh_primo(3)
    True
    >>> eh_primo(4)
    False
    """

    # por definição
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def quais_primos(num):
    """
    >>> quais_primos(13)
    [2, 3, 5, 7, 11]
    """
    return [n for n in range(2, num) if eh_primo(n)]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
