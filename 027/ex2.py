"""
Problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/1255

Entrada:
'Computers account for only 5% of the country's commercial electricity consumption'
Saída:
'co'

Entrada:
'Input'
Saída:
'inptu'

Entrada:
'frequency letters'
Saída:
'e'


>>> count_max_occurrence('Input')
'inptu'

>>> count_max_occurrence("Computers account for only 5% of the country's commercial electricity consumption")
'co'

>>> count_max_occurrence('frequency letters')
'e'

"""

def count_max_occurrence(sentence):
    letter_count = {}

    sorted_sentence = sorted(sentence.lower())

    for letter in sorted_sentence:
        if letter.isalpha():
            if letter not in letter_count.keys():
                letter_count[letter] = 1
            else:
                letter_count[letter] += 1

    max_value = max(letter_count.values())

    word = ''

    for k, v in letter_count.items():
        if v == max_value:
            word += k
    
    return "".join(sorted(word))