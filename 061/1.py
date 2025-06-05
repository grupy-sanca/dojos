"""
Wordle é um jogo administrado pelo NY Times que ficou extremamente popular durante a pandemia.
Nele, o jogador precisa adivinhar uma palavra secreta de 5 letras, recebendo como feedback
as letras na cor amarela caso elas existam na palavra, e na cor verde caso não só elas existam
na palavra quanto ele acertou a exata posição dela.
Como um exemplo, caso a palavra secreta seja AVIÃO, mas o jogador chutou a palavra CALVO,
as letras A e V ficariam amarela, pois a palavra secreta tem a letra A e a letra V, porém não
naquelas posições. Já a letra O ficaria verde, pois a palavra secreta possui a letra O
exatamente naquela posição. As letras C e L não fazem parte da palavra, portanto, ficariam cinza.

Crie uma função que receba duas palavras, a secreta e a tentativa, nessa ordem, e
retorne um dicionário onde as chaves são as cores, e os valores são listas de letras,
agrupando cada letra na sua respectiva cor de resposta.

Ignore acentos e palavras compostas.

wordle("AVIAO", "CALVO")
{'amarelo': ['A', 'V'], 'verde': ['O'], 'cinza': ['C', 'L']}

wordle("NAVIO", "AVIAO")
{'amarelo': ['A', 'V', 'I'], 'verde': ['O'], 'cinza': ['A']}

Cuidado: quando a tentativa possuir letras repetidas, elas têm que ser tratadas separadamente.
No segundo exemplo, já foi encontrado um A da palavra AVIAO na palavra NAVIO,
portanto, o segundo A não pode ser encontrado, caindo na lista de letras cinza.

>>> wordle("ABCDE", "FFFFF")
{'amarelo': [], 'verde': [], 'cinza': ['F', 'F', 'F', 'F', 'F']}

>>> wordle("ABCDF", "FFFFF")
{'amarelo': [], 'verde': ['F'], 'cinza': ['F', 'F', 'F', 'F']}

>>> wordle("AVIAO", "CALVO")
{'amarelo': ['A', 'V'], 'verde': ['O'], 'cinza': ['C', 'L']}

>>> wordle("NAVIO", "AVIAO")
{'amarelo': ['A', 'V', 'I'], 'verde': ['O'], 'cinza': ['A']}

>>> wordle("AVIAO", "NAVIO")
{'amarelo': ['A', 'V', 'I'], 'verde': ['O'], 'cinza': ['N']}
""" 

def wordle(alvo, chute):
    resultado = {'amarelo': [], 'verde': [], 'cinza': []}
    dict_alvo = {}
    verdes = set()
    for idx, letra in enumerate(alvo):
        if alvo[idx] == chute[idx]:
            resultado['verde'].append(letra)
            verdes.add(idx)
            continue
        dict_alvo[letra] = dict_alvo.get(letra, 0) + 1
    for idx, letra in enumerate(chute):
        if idx in verdes:
            continue
        if dict_alvo.get(letra, 0) > 0:
            resultado['amarelo'].append(letra)
        else:
            resultado['cinza'].append(letra)
        dict_alvo[letra] = dict_alvo.get(letra, 0) - 1
    return resultado