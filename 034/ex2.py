"""
hamekame ka

>>> teste('hamekame')
'ka'

>>> teste('haamekaame')
'kaaaa'

>>> teste('haaamekaame')
'kaaaaaa'

>>> teste('haaaamekaaame')
'kaaaaaaaaaaaa'
"""


def teste(palavra):
    contador_1 = conta_a(palavra[1:])
    contador_2 = conta_a(palavra[-3::-1])
    return forma_ka_final(contador_1 * contador_2)


def conta_a(palavra):
    contador = 0
    for i in palavra:
        if i == 'a':
            contador += 1
        else:
            break

    return contador


def forma_ka_final(a_total):
    return 'k' + 'a' * a_total



