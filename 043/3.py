"""
>>> get_adjacents("1")
['1', '2', '4']

>>> get_adjacents("2")
['1', '2', '3', '5']

>>> get_pin("01")
['01', '02', '04', '81', '82', '84']

"""

def get_adjacents(digit):
    keypad = {'0': ['0', '8'],
              '1': ['1','2','4'],
              '2': ['1','2','3', '5'],
              '3': ['2', '3', '6'],
              '4': ['1', '4', '5', '7'],
              '5': ['2', '4', '5', '6', '8'],
              '6': ['3', '5', '6', '9'],
              '7': ['4', '7', '8'],
              '8': ['0','5', '7', '8', '9'],
              '9': ['6', '8', '9']}
    return keypad[digit]


def get_pin(pin):
    resposta = []
    for digito in pin:
     for valor in get_adjacents(digito):
        possible_pin = 'valor'
        for valor_2 in resposta_parcial:
            resposta.append()
