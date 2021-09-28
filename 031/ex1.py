"""
https://www.codewars.com/kata/5914e068f05d9a011e000054

It gets a string:
string="aaaaaaaabaaaa"
And generates an array that sums all the repeating characters like so:
compressed=[[8,"a"],[1,"b"],[4,"a"]]
The compressed version is turned into a string:
compressed='[[8,"a"],[1,"b"],[4,"a"]]'

Finally,
If the compressed version is shorter than the original string, the function will return the compressed version.
Otherwise it will return the original string.

Example1:
string1="aaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaa"
output1='[[26,"a"],[1,"b"],[18,"a"]]'

Example2:
string2="abcde"
output2="abcde"

After you created the compression algorithm, create a decompression algorithm:

It gets a string (output1, output2, etc.).
If the string is comrpessed, it returns the uncompressed version,
If it is uncompressed, it returns the original string unchanged. 


>>> comprime("abcde")
'abcde'

>>> comprime("aaaaaaaaaaaaaaaaaaaa")
'[[20, "a"]]'

>>> comprime("aaaaaaaaaaaaaaaaaaaab")
'[[20, "a"],[1, "b"]]'

>>> comprime ("abbbb")
'abbbb'

>>> comprime("aaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaa")
'[[26, "a"],[1, "b"],[18, "a"]]'


>>> descomprime('[[20, "a"]]')
'aaaaaaaaaaaaaaaaaaaa'

>>> descomprime('[[26, "a"],[1, "b"],[18, "a"]]')
'aaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaa'

>>> descomprime(comprime('aaaaaabbbbbcccdefghhhhhhhhhhhhhhhhhhhhhhhhiiiiiiiiiiiiiiiiiii'))
'aaaaaabbbbbcccdefghhhhhhhhhhhhhhhhhhhhhhhhiiiiiiiiiiiiiiiiiii'

>>> descomprime(comprime ("abbbb"))
'abbbb'

"""
import ast


def comprime(string):
    lista = []
    letra_atual = string[0]
    contador = 0
    for i, letter in enumerate(string):
        if letter == letra_atual:
            contador += 1
        else:
            lista.append([contador,letra_atual])
            letra_atual = letter
            contador = 1
        if i == len(string) - 1:
            lista.append([contador, letra_atual])
    string_comprimida = "["
    for elemento in lista:
        string_comprimida += f'[{elemento[0]}, "{elemento[1]}"],'
    string_comprimida = string_comprimida[:-1]
    string_comprimida += "]"

    if len(string) < len(string_comprimida):
        return string
    return string_comprimida

def descomprime(string_comprimida):
    if not string_comprimida.startswith("["):
        return string_comprimida
   # pares = string_comprimida[1:-1].split("[")[1:]
   # pares = [[int(par.split(', "')[0]),par.split(', "')[1][0]] for par in pares]
   # return "".join(f"{par[0] * par[1]}" for par in pares)   

    lista = ast.literal_eval(string_comprimida)
    return "".join(f"{par[0] * par[1]}" for par in lista)