"""
Verificar se uma String é um Pangrama:
Um pangrama é uma frase que contém todas as letras do alfabeto pelo menos uma vez.
Escreva uma função que verifique se uma determinada string é um pangrama.

Entrada:
"The quick brown fox jumps over the lazy dog"

Saída:
True

>>> eh_pangrama("The quick brown fox jumps over the lazy dog")
True

>>> eh_pangrama("Nao eh um pangrama")
False
>>> eh_pangrama("Nao eh um pangrama")
False
"""

def eh_pangrama(string):
    letter_count = {}
    string = string.lower().replace(" ", "")
    
    for letter in string:
        letter_count[letter] = None
    
    return len(letter_count) == 26
