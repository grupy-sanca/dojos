"""
http://facweb.cs.depaul.edu/sjost/it212/documents/ascii-pr.htm

23511011501782351112179911801562340161171141148

inverte:
84114117116104326510811997121115328710511011532

percorre 3 se começa com 1 e percorre 2 caso contrário:
84 114 117 116 104 32 65 108 119 97 121 115 32 87 105 110 115 32

converte tudo para string usando chr()

>>> ord("z")
122
>>> chr(122)
'z'


>>> to_ascii("48")
'T'

>>> to_ascii("4848")
'TT'

>>> to_ascii("484848")
'TTT'

>>> to_ascii("41148")
'Tr'

>>> to_ascii("4871141148")
'TruT'

>>> to_ascii("23511011501782351112179911801562340161171141148")
'Truth Always Wins '
"""

def to_ascii(value):
    result = ""
    inverted = value[::-1]
    for current in separate_in_ascii_chars(inverted):
        result += chr(current)
    return result


def separate_in_ascii_chars(chars):
    i = 0
    while i < len(chars):
        offset = 3 if chars[i] == '1' else 2
        yield int(chars[i:i + offset])
        i += offset