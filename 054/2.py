"""
2 - Agora que sabemos como é a estrutura de uma das cadeias do DNA, devemos lembrar que uma molécula
de DNA é composta por duas cadeias, formando uma dupla hélice. Mais do que isso, essas duas cadeias
são interligadas pelas conexões de suas bases. Cada base se conecta com outra de acordo com um pareamento
específico:
A <--> T (Adenina se conecta com Timina, e vice-versa)
C <--> G (Citosina se conecta com Guanina, e vice-versa)

Portanto, se tivermos duas cadeias de DNA, precisamos ter certeza de que são cadeias válidas,
ou seja, que cada par de conexões é um par válido.

Vamos criar uma função que verifica se duas cadeias de DNA formam uma molécula válida de DNA,
onde suas bases estão ordenadas de forma que todas as conexões são válidas.

Exemplos:
valida_dna(['A', 'T', 'G'], ['T', 'A', 'C']) --> True
valida_dna(['A', 'T', 'G'], ['T', 'S', 'C']) --> False (S não é uma base válida)
valida_dna(['A', 'T', 'G'], ['T', 'A']) --> False (As duas cadeias não têm o mesmo tamanho)
valida_dna(['A', 'T', 'G'], ['T', 'A', 'T']) --> False (G <--> T não é uma conexão válida)

>>> valida_dna(['A', 'T', 'G'], ['T', 'A', 'C'])
True

>>> valida_dna(['A', 'T', 'G'], ['T', 'S', 'C'])
False

>>> valida_dna(['A', 'T', 'G'], ['T', 'A'])
False

>>> valida_dna(['A', 'T', 'G'], ['T', 'A', 'T'])
False

>>> valida_base(['A', 'T', 'G'])
True

>>> valida_base(['T', 'S', 'C'])
False

>>> valida_tamanhos(['A', 'T'], ['G', 'C'])
True

>>> valida_tamanhos(['A'], [])
False

>>> valida_conexao('A', 'T')
True

>>> valida_conexao('A', 'G')
False
"""


def valida_base(cadeia):
    bases_usuario = set(cadeia)
    bases_unicas = {'A', 'C', 'G', 'T'}
    return bases_usuario.issubset(bases_unicas)


def valida_tamanhos(cadeia1, cadeia2):
    return len(cadeia1) == len(cadeia2)


def valida_conexao(base1, base2):
    mapeamento = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G',
    }

    return mapeamento[base1] == base2


def valida_dna(cadeia1: list[str], cadeia2: list[str]):
    if not valida_tamanhos(cadeia1, cadeia2):
        return False
   
    # if not valida_base(cadeia1) or not valida_base(cadeia2):
    #     return False
    
    for b1, b2 in zip(cadeia1, cadeia2):
        try:
            if not valida_conexao(b1, b2):
                return False
        except KeyError:
            return False
    return True
