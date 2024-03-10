"""
5 3
w l
s m
e o
a b
c z
mbs loww 2017
tozwbde ceoire
ifmuwdosinbm

>> mapeia_letras([('w','l'),('s','m'),('e','o'),('a','b'),('c','z')])
{'w': 'l', 's': 'm', 'e': 'o', 'a': 'b', 'c': 'z',}

>>> mapeia_letras([('a', 'e'), ('b', 'c')])
{'a': 'e', 'e': 'a', 'b': 'c', 'c': 'b'}

>>> converte_frase('mbs loww 2017', [('w','l'),('s','m'),('e','o'),('a','b'),('c','z')])
'sam well 2017'

>>> converte_frase('tozwbde ceoire', [('w','l'),('s','m'),('e','o'),('a','b'),('c','z')])
'teclado zoeiro'

>>> converte_frase('ifmuwdosinbm', [('w','l'),('s','m'),('e','o'),('a','b'),('c','z')])
'ifsuldeminas'
"""


def mapeia_letras(letras):
    mapeamento = {}
    for chave, valor in letras:
        mapeamento[chave] = valor
        mapeamento[valor] = chave
    return mapeamento


def converte_frase(frase, letras):
    mapeamento = mapeia_letras(letras)
    return "".join([mapeamento.get(letra, letra) for letra in frase])
