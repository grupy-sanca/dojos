"""
Dojo 067 - A Festa Junina

Exercício 3: O Labirinto de Milho

Depois de organizar a quadrilha, você descobre que a próxima pista leva a um labirinto de milho!
Para chegar à festa, você precisa encontrar o caminho mais curto da entrada ('E') até a saída ('S').

O labirinto é representado por uma matriz de caracteres, onde:
- ' ' é um caminho livre
- '#' é uma parede (milho alto demais!)
- 'E' é a entrada
- 'S' é a saída

Escreva uma função `encontrar_caminho_curto(labirinto)` que recebe o labirinto e retorna
uma lista de tuplas com as coordenadas (linha, coluna) do caminho mais curto da entrada até a saída.
Se não houver caminho, a função deve retornar uma lista vazia.

Exemplos de Teste:

1.  Labirinto simples:
    - Entrada:
      ```
      labirinto = [
          ['E', ' ', 'S']
      ]
      ```
    - Saída esperada: `[(0, 0), (0, 1), (0, 2)]`

2.  Labirinto com obstáculo:
    - Entrada:
      ```
      labirinto = [
          ['E', '#', 'S'],
          [' ', ' ', ' ']
      ]
      ```
    - Saída esperada (um dos caminhos mais curtos): `[(0, 0), (1, 0), (1, 1), (1, 2), (0, 2)]`

3.  Labirinto sem saída:
    - Entrada:
      ```
      labirinto = [
          ['E', '#'],
          ['#', 'S']
      ]
      ```
    - Saída esperada: `[]`

4.  Labirinto maior (teste o comprimento do caminho):
    - Entrada:
      ```
      labirinto = [
          ['E', ' ', '#', ' '],
          [' ', '#', ' ', ' '],
          [' ', ' ', ' ', '#'],
          ['#', '#', ' ', 'S']
      ]
      ```
    - Saída esperada: Uma lista de coordenadas. O caminho mais curto tem 8 passos (comprimento 9).

Desenvolva a função `encontrar_caminho_curto` e os testes correspondentes.

>>> encontrar_item([['E', '#'],['#', 'S']],'E')
(0, 0)

>>> encontrar_item([['E', '#'],['#', 'S']],'S')
(1, 1)

"""



def encontrar_item(mapa, item):
    i=0
    j=0
    for linha in mapa: 
        for coluna in linha:
           if coluna ==item:
                return (i,j)
           j+=1
        i+=1
        j=0
    return None

def nos_adjacentes_validos(mapa, no, explorados):
    adjacentes=[]
    
    no_x, no_y = no
    len_x = len(mapa)
    len_y = len(mapa[[0]])


    for x,y in [(no_x -1 , no_y),(no_x , no_y -1),(no_x +1, no_y ),(no_x , no_y +1) ]:
        
        if (0 <= x < len_x and 0 <= y < len_y) and mapa[x][y] != "#" and (x,y) not in explorados:
            adjacentes.append((x,y))

    return adjacentes


def constroi_mapa(mapa):
    fila_exploracao = []
    lista_explorados = []

    raiz = encontrar_item(mapa, "E", lista_explorados)
    



    
    
    pass