"""
Você provavelmente conhece o sistema de "curtidas" do Facebook e de outras páginas.
As pessoas podem "curtir" postagens de blog, fotos ou outros itens.
Queremos criar o texto que deve ser exibido ao lado de um item com base nas curtidas.

Implemente uma função que recebe uma lista contendo os nomes das pessoas que curtiram um item.
Ela deve retornar o texto a ser exibido conforme mostrado nos exemplos:

Entrada:
[]

Saída:
'ninguém curtiu isso'

Entrada:
["Peter"]

Saída:
'Peter curtiu isso'

Entrada:
["Jacob", "Alex"]

Saída:
'Jacob e Alex curtiram isso'

Entrada:
["Max", "John", "Mark"]

Saída:
'Max, John e Mark curtiram isso'

Entrada:
["Alex", "Jacob", "Mark", "Max"]

Saída:
'Alex, Jacob e mais 2 pessoas curtiram isso'

Nota: Para 4 ou mais nomes, o número em "e mais 2 pessoas" simplesmente aumenta.

>>> mostra_curtidas([])
'ninguém curtiu isso'

>>> mostra_curtidas(["Peter"])
'Peter curtiu isso'

>>> mostra_curtidas(["Jacob", "Alex"])
'Jacob e Alex curtiram isso'

>>> mostra_curtidas(["Max", "John", "Mark"])
'Max, John e Mark curtiram isso'

>>> mostra_curtidas(["Alex", "Jacob", "Mark", "Max"])
'Alex, Jacob e mais 2 pessoas curtiram isso'

>>> mostra_curtidas(["Alex", "Jacob", "Mark", "Max", "A", "A"])
'Alex, Jacob e mais 4 pessoas curtiram isso'

>>> mostra_curtidas(["Alex", "Jacob"] * 200)
'Alex, Jacob e mais 398 pessoas curtiram isso'
"""


def mostra_curtidas(nomes):
    match nomes:
        case []:
            return "ninguém curtiu isso"
        case [n1]:
            return f"{n1} curtiu isso"
        case [n1, n2]:
            return f"{n1} e {n2} curtiram isso"
        case [n1, n2, n3]:
            return f"{n1}, {n2} e {n3} curtiram isso"
        case [n1, n2, *outros]:
            return f"{n1}, {n2} e mais {len(outros)} pessoas curtiram isso"
