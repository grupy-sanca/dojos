"""

>>> teste('Tpo oCder')
'TopCoder'

>>> teste('aa bb')
'abab'


>>> teste('aaa bb')
'ababa'
"""


def teste(entrada):
    palavra1, palavra2 = entrada.split()
    # a, b = entrada.split()

    # return "".join([i+j for i,j in zip(a,b)])+a[min(len(a),len(b)):]+b[min(len(a),len(b)):]

    palavra3 = ''

    if len(palavra2) >= len(palavra1):
        palavra3 = palavra_final(palavra1,palavra2,len(palavra1),palavra2)

    else:
        palavra3 = palavra_final(palavra1,palavra2,len(palavra2),palavra1)

    return palavra3

def palavra_final(palavra_1,palavra_2, comprimento_menor, palavra_maior):
        palavra3 =''
        for l1,l2 in zip(palavra_1,palavra_2):
            palavra3 += l1 + l2

        palavra3 += palavra_1[comprimento_menor:]+palavra_2[comprimento_menor:]     
        return palavra3   







