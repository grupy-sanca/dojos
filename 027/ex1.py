"""
Problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/1234


Entrada:
'This is a dancing sentence'

Saída:
'ThIs Is A dAnCiNg SeNtEnCe'

Entrada: 
'  This   is         a  dancing   sentence'

Saída:
'  ThIs   Is         A  dAnCiNg   SeNtEnCe'

Entrada:
aaaaaaaaaaa

Saída
AaAaAaAaAaA


>>> dancing_string('This is a dancing sentence')
'ThIs Is A dAnCiNg SeNtEnCe'

>>> dancing_string('  This   is         a  dancing   sentence')
'  ThIs   Is         A  dAnCiNg   SeNtEnCe'

>>> dancing_string('aaaaaaaaaaa')
'AaAaAaAaAaA'

"""


def dancing_string(sentence):
    response = ''

    dancing_flag = True

    for letter in sentence:
        if letter.isalpha():
            response += letter.upper() if dancing_flag else letter.lower()
            dancing_flag = not dancing_flag
        else:
            response += ' '

    return response

