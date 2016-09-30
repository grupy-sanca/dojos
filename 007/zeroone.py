'''
Problema Zero or One retirado do URI
(https://www.urionlinejudge.com.br/judge/en/problems/view/1467)

>>> vencedor(0, 0, 0)
'*'

>>> vencedor(0, 0, 1)
'C'

>>> vencedor(0, 1, 0)
'B'

>>> vencedor(0, 1, 1)
'A'

>>> vencedor(1, 0, 0)
'A'

>>> vencedor(1, 0, 1)
'B'

>>> vencedor(1, 1, 0)
'C'

>>> vencedor(1, 1, 1)
'*'
'''


def vencedor(a, b, c):
    '''
    Verifica se existe um vencedor
    e retorna a letra do vencedor ou *
    '''
    if a == b != c:
        return 'C'
    elif b == c != a:
        return 'A'
    elif a == c != b:
        return 'B'
    else:
        return '*'


def main():
    entrada = ''
    while entrada is not None:
        try:
            entrada = input()
        except EOFError:
            return
        entrada = entrada.split()
        print(vencedor(*entrada))


if __name__ == "__main__":
    main()
