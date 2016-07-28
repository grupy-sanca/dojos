def converte(string):
    """
    >>> converte("abc")
    'cba'
    """
    return string[::-1]

if __name__ == '__main__':
    import sys
    import doctest; doctest.testmod()
    converte(sys.argv[1])
