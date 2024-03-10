"""
Você tem um robô que foi programado para andar segundo uma programação.
As instruções são strings, devem ser enviadas através de uma lista, e cada
instrução deve conter uma letra (N de Norte, S de Sul, L de Leste ou O de Oeste)
e um número de passos. Por exemplo:
- ["N 10", "L 20", "S 5", "O 12"]

O robô começa na posição (0, 0) e segue todos os passos das suas instruções.
No exemplo anterior, ele terminaria a execução da sua programação na posição (8, 5).

Crie uma função que faz a previsão de onde o robô irá parar, dado a lista de
instruções que ele irá seguir.

Exemplos:
- previsao_robo(["N 10", "L 20", "S 5", "O 12"]) --> (8, 5)
- previsao_robo(["O 7", "N 12", "L 2"]) --> (-5, 12)
- previsao_robo(["S 3"]) --> (0, -3)
- previsao_robo([]) --> (0, 0)

>>> pega_comando("N 10")
('N', 10)

>>> pega_comando("L 20")
('L', 20)

>>> pega_programacao(["N 10", "L 20", "S 5", "O 12"])
[('N', 10), ('L', 20), ('S', 5), ('O', 12)]

>>> pega_programacao(["O 7", "N 12", "L 2"])
[('O', 7), ('N', 12), ('L', 2)]

>>> move_robo((0, 0) , 'S', 2)
(0, -2)

>>> move_robo((0, -2) , 'L', 4)
(4, -2)

>>> previsao_robo(["N 10", "L 20", "S 5", "O 12"])
(8, 5)

>>> previsao_robo(["O 7", "N 12", "L 2"])
(-5, 12)

>>> previsao_robo(["S 3"])
(0, -3)

>>> previsao_robo([])
(0, 0)
"""

def pega_comando(comando):
    direcao, valor = comando.split()
    return direcao, int(valor)


def pega_programacao(lista_de_comandos):
    return [pega_comando(comando) for comando in lista_de_comandos]


def move_robo(posicao_inicial, direcao, valor):
    mapeamento = {'L': (1, 0), 'O': (-1, 0), 'N': (0, 1), 'S': (0, -1)}
    return tuple([base * valor + coordenada for base, coordenada in zip(mapeamento[direcao], posicao_inicial)])

    # if direcao == 'L':
    #     nova_posicao = (posicao_inicial[0] + valor, posicao_inicial[1])
    # if direcao == 'O':
    #     nova_posicao = (posicao_inicial[0] - valor, posicao_inicial[1])
    # if direcao == 'N':
    #     nova_posicao = (posicao_inicial[0], posicao_inicial[1] + valor)
    # if direcao == 'S':
    #     nova_posicao = (posicao_inicial[0], posicao_inicial[1] - valor)
    # return nova_posicao

def previsao_robo(lista_de_comandos):
    posicao = (0, 0)
    for direcao, valor in pega_programacao(lista_de_comandos):
        posicao = move_robo(posicao, direcao, valor)
    return posicao
