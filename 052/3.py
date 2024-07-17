"""
Todos estão prontos para assistir a apresentação, mas será que todos conseguem ver o palco?
Dado uma lista de listas, cada lista interna representa uma fileira de assentos no teatro.
As listas são preenchidas com as alturas de cada uma das pessoas sentadas na cadeira.
As pessoas da fileira de trás só conseguem assistir a apresentação confortavelmente se
são estritamente mais altas do que as pessoas da fileira da frente.

Escreva uma função que consegue dizer se todas as pessoas no teatro conseguirão assistir a apresentação.

- todos_veem_palco([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]) --> True
- todos_veem_palco([
  [0, 1, 1],
  [1, 2, 4],
  [3, 6, 5]
]) --> True
- todos_veem_palco([
  [0, 2, 1],
  [2, 3, 2],
  [3, 2, 4]
]) --> False (a pessoa de altura 2 na última fileira está atrás de alguém de altura 3)
- todos_veem_palco([
  [0, 2, 3],
  [4, 3, 3],
  [5, 5, 5]
]) --> False (a pessoa de altura 3 na segunda fileira está atrás de alguém de altura 3)


>>> todos_veem_palco([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
True

>>> todos_veem_palco([[0, 2, 1],[2, 3, 2],[3, 2, 4]])
False

>>> todos_veem_palco([[0, 2, 3],[4, 3, 3],[5, 5, 5]])
False

"""

def todos_veem_palco(plateia):
    for x, y, z in zip(*plateia):
        if not (z > y > x):
            return False
    return True
