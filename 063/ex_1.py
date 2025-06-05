"""
Uma das estruturas de dados mais famosa é a Pilha. Ela organiza os dados seguindo a regra "o último a entrar é o primeiro
a sair" (Last In, First Out, ou LIFO).
Vamos construir uma classe que instancie um objeto Pilha.
A Pilha deve ter os métodos colocar() e retirar().
O método "colocar" recebe como parâmetro um dado, coloca este dado no final da pilha e retornar a pilha atualizada.
O método "retirar" pode receber como parâmetro um valor numérico N, e deve retornar os últimos N dados da pilha em ordem
reversa. Os dados retornados devem ser removidos da pilha. Caso não seja informado o parâmetro N, assume-se que o valor seja 1.

Assuma que todos os dados enviados para a pilha são caracteres alfanuméricos em caixa alta.

Para inicializar uma nova pilha
>>> pilha = Pilha()

>>> pilha.colocar('A')
['A']

>>> pilha.colocar('3')
['A', '3']

>>> pilha.colocar('Y')
['A', '3', 'Y']

>>> pilha.retirar(2)
['Y', '3']

>>> pilha.retirar()
['A']

Tentar retirar itens de uma pilha vazia retorna uma pilha vazia
>>> pilha.retirar()
[]

"""


class Pilha():
    
    def __init__(self) -> None:
        self.pilha = []

    def colocar(self, elem: str) -> list:
        self.pilha.append(elem)
        return self.pilha

    def retirar(self, n: int = 1) -> list:
        self.pilha, resposta = self.pilha[:-n], self.pilha[-n:]
        resposta.reverse()
        return resposta
