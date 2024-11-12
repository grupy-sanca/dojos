"""
Dada uma lista como argumento, complete a função contar_sorrisos(), que deve retornar o número
total de carinhas sorridentes.

Regras para uma carinha sorridente:

    Cada carinha deve conter um par válido de olhos. Os olhos podem ser representados por : ou ;
    Uma carinha pode ter um nariz, mas não é obrigatório. Caracteres válidos para o nariz são - ou ~
    Cada carinha sorridente deve ter uma boca sorridente, que deve ser marcada com ) ou D

Nenhum outro caractere além dos mencionados é permitido.

Exemplos válidos de carinhas sorridentes: :), :D, ;-D, :~) Exemplos inválidos de carinhas: ;(, :>, :}, :]

Exemplos:

Entrada:
contar_sorrisos([':)', ';(', ';}', ':-D'])

Saída:
2

Entrada:
contar_sorrisos([';D', ':-(', ':-)', ';~)'])

Saída:
3

Entrada:
contar_sorrisos([';]', ':[', ';*', ':$', ';-D'])

Saída:
1

Caso a lista esteja vazia, retorne 0.

>>> contar_sorrisos([])
0

>>> contar_sorrisos([':)'])
1

>>> contar_sorrisos([':)', ':('])
1

>>> eh_sorriso(':)')
True

>>> eh_sorriso(':{')
False

>>> eh_sorriso(';0)')
False

>>> eh_sorriso(';-)')
True

>>> eh_sorriso(';')
False

>>> eh_sorriso(';-))')
False

>>> contar_sorrisos([':)', ';(', ';}', ':-D'])
2

>>> contar_sorrisos([';D', ':-(', ':-)', ';~)'])
3

>>> contar_sorrisos([';]', ':[', ';*', ':$', ';-D'])
1

>>>
"""
import re

def eh_sorriso(carinha):
    return re.match('^[;:][-~]?[)D]$', carinha) is not None

def contar_sorrisos(carinhas):
    return sum(eh_sorriso(c) for c in carinhas)
