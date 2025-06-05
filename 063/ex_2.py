"""
1 - Agora que temos nossa Pilha, vamos criar uma Pilha com Prioridade.
Nessa Pilha, vamos ter um método adicional chamado "prio", onde queremos retirar primeiro os NÚMEROS, caso eles existam na pilha.

Assuma que todos os dados enviados para a pilha são caracteres alfanuméricos em caixa alta.

Para inicializar uma nova pilha
>>> pilha = PilhaPrio()

>>> pilha.numeros
[]

>>> pilha.colocar('A')
['A']

>>> pilha.colocar('3')
['A', '3']

>>> pilha.numeros
[1]

>>> pilha.colocar('Y')
['A', '3', 'Y']

>>> pilha.prio()
['3']

>>> pilha.is_number('1')
True

>>> pilha.is_number('Y')
False

>>> pilha.retirar(2)
['Y', 'A']

Caso haja mais de um número, o método prio retira eles primeiro, até que não haja mais nenhum número.
['7', 'A', '3', 'Y']

>>> pilha.pilha = ['A','Y']
>>> pilha.prio()
['Y']

>>> pilha.pilha = ['7', 'A', '3', 'Y']
>>> pilha.numeros = [0, 2]

>>> pilha.prio(3)
['3', '7', 'Y']

Atenção aos números duplicados, pois deve-se retirar a última ocorrência
['7', 'A', '7', 'Y']

>>> pilha.pilha = ['7', 'A', '7', 'Y']
>>> pilha.numeros = [0, 2]

>>> pilha.prio()
['7']

>>> pilha.retirar(3)
['Y', 'A', '7']

>>> pilha.pilha = ['3', 'A', '7', 'Y']
>>> pilha.numeros = [0, 2]

>>> pilha.retirar(3)
['Y', '7', 'A']

>>> pilha.prio()
['3']

>>> pilha.prio()
[]

>>> pilha.prio()
[]

>>> pilha.retirar()
[]

"""
from ex_1 import Pilha


class PilhaPrio(Pilha):

    def __init__(self) -> None:
        super().__init__()
        self.numeros = []

    def is_number(self, item: str) -> bool:
        return item.isnumeric()
    
    def colocar(self, elem: str):
        if self.is_number(elem):
            self.numeros.append(len(self.pilha))

        return super().colocar(elem)

    def prio(self, n: int = 1) -> list:
        resposta = []
        for i in range(n):
            if self.numeros:
                resposta.append(self.pilha.pop(self.numeros.pop()))
            else:
                resposta.extend(self.retirar())

        return resposta

    def retirar(self, n: int = 1) -> list:
        resposta = super().retirar(n)
        if self.numeros:
            while self.numeros[-1] > len(self.pilha):
                self.numeros.pop()
        return resposta
