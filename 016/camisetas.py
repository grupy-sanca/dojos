"""
>>> VAR = "Maria Joao\\nbranco P\\nMarcio Guess\\nvermelho P\\nMaria Jose\\nbranco P"
>>> var = "Maria Joao\\nbranco P"
>>> separa(var)
[('branco', 'P', 'Maria Joao')]
>>> separa(VAR)
[('branco', 'P', 'Maria Joao'), ('vermelho', 'P', 'Marcio Guess'), ('branco', 'P', 'Maria Jose')]
>>> ordena([('branco', 'P', 'Maria Joao'), ('vermelho', 'P', 'Marcio Guess'), ('branco', 'P', 'Maria Jose')])
[('branco', 'P', 'Maria Joao'), ('branco', 'P', 'Maria Jose'), ('vermelho', 'P', 'Marcio Guess')]
>>> ordena([('branco', 'M', 'Maria Joao'), ('vermelho', 'P', 'Marcio Guess'), ('branco', 'P', 'Maria Jose')])
[('branco', 'P', 'Maria Jose'), ('branco', 'M', 'Maria Joao'), ('vermelho', 'P', 'Marcio Guess')]
>>> VAR2 = "Maria Jose\\nbranco P\\nMangojata Mancuda\\nvermelho P\\nCezar Torres Mo\\nbranco P\\nBaka Lhau\\nvermelho P\\nJuJu Mentina\\nbranco M\\nAmaro Dinha\\nvermelho P\\nAdabi Finho\\nbranco G\\nSeverina Rigudinha\\nbranco G\\nCarlos Chade Losna"
>>> ordena(separa(VAR2))
[('branco', 'P', 'Cezar Torres Mo'), ('branco', 'P', 'Maria Jose'), ('branco', 'M', 'JuJu Mentina'), ('branco', 'G', 'Adabi Finho'), ('branco', 'G', 'Severina Rigudinha'), ('vermelho', 'P', 'Amaro Dinha'), ('vermelho', 'P', 'Baka Lhau'), ('vermelho', 'P', 'Mangojata Mancuda')]
"""


def separa(text):
    lista = text.split("\n")
    result = []
    for nome, corT in zip(lista[::2], lista[1::2]):
        cor, tamanho = corT.split()
        result.append((cor, tamanho, nome))
    return result


def ordena(lista):
    return sorted(sorted(sorted(lista, key=lambda x: x[2]), key=lambda x: x[1], reverse=True), key=lambda x: x[0])