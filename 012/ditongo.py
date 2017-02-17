"""
Recebe uma string e retira vogais consecutivas, por exemplo:
    CAASO -> CASO
    PEIDO -> PEDO
    CASA -> CASA

>>> remove_ditongo('CAASO')
'CASO'
>>> remove_ditongo('PEIDO')
'PEDO'
>>> remove_ditongo('caaso')
'caso'
>>> remove_ditongo('Peido')
'Pedo'
>>> remove_ditongo('Casa')
'Casa'
>>> remove_ditongo ('283874')
'283874'
>>> remove_ditongo ('')
''
"""

VOGAIS = ('A', 'E', 'I', 'O', 'U')


def remove_ditongo(palavra):
    palavra_sem_ditongos = ''
    ult = None
    for c in palavra:
        if not(c.upper() in VOGAIS) or not(ult.upper() in VOGAIS):
            palavra_sem_ditongos += c
        ult = c

    return palavra_sem_ditongos
