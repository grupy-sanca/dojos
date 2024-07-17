"""
3 - Dentro da célula há uma organela chamada Ribossomo, que é responsável
por decodificar as instruções do DNA e construir proteínas à partir dessas instruções.

Para isso, o Ribossomo executa algumas tarefas:
- Constroi um RNA mensageiro, que é gerado à partir do DNA
- Conecta vários RNA de transferência ao RNA mensageiro

O RNA é uma cadeia muito similar ao DNA, entretanto ele não possui Timina, e sim Uracila (U).
O RNA mensageiro é gerado à partir do pareamento no DNA:

rna_mensageiro(['A', 'T', 'G']) --> ['U', 'A', 'C']

Perceba que, no RNA, quem se conecta com a Adenina é a Uracila.

O RNA de transferência possui um aminoácido conectado à ele. Cada tRNA é formado por um grupo de 3 bases,
e transporta um tipo único de aminoácido.

rna_transferencia('AAA') --> 'aa0'
rna_transferencia('UAG') --> 'aa50'

Vamos construir uma função que simula um ribossomo, onde a entrada é uma sequência de DNA,
e a saída é uma sequência de aminoácidos.

Exemplo:
ribossomo(['A', 'T', 'G']) --> ['aa49']
ribossomo(['G', 'C', 'A', 'T', 'A', 'T']) --> ['aa27', 'aa12']
ribossomo(['G', 'C', 'A', 'T', 'A']) --> ['aa27'] (Os dois que sobram não são suficientes para invocar um tRNA)

Dica #1: a cadeia 'lista' recebida em ribossomo(lista) deve ser transformada em RNA mensageiro,
rna_mensageiro(lista), para então ter seus pedaços de tamanho 3 convertidos em
aminoácidos usando rna_transferencia()


Dica #2: função rna_transferencia():

>>> rna_mensageiro(['A', 'T', 'G'])
['U', 'A', 'C']

>>> rna_mensageiro(['A', 'A', 'G'])
['U', 'U', 'C']

>>> gerar_ribossomo(['A', 'T', 'G'])
['aa49']

>>> gerar_ribossomo(['G', 'C', 'A', 'T', 'A', 'T'])
['aa27', 'aa12']

>>> gerar_ribossomo(['G', 'C', 'A', 'T', 'A', 'T', 'A'])
['aa27', 'aa12']
"""
from itertools import count, product, batched


def rna_transferencia(key: str):
    if len(key) != 3:
        return ''

    value = count(0)
    t = {''.join(key): f'aa{next(value)}' for key in product(['A', 'C', 'G', 'U'], repeat=3)}
    return t.get(key, '')


def rna_mensageiro(sequencia: list[str]) -> list[str]:
    mapeamento = {
        'A': 'U',
        'T': 'A',
        'G': 'C',
        'C': 'G',
    }
    return [mapeamento[key] for key in sequencia]


def gerar_ribossomo(sequencia_dna: list[str]) -> list[str]:
    # sequencia_rna = rna_mensageiro(sequencia_dna)
    # aminoacidos = []
    

    # for idx in range(0, len(sequencia_rna), 3):
    #     if idx+3 <= len(sequencia_rna):
    #         aminoacidos.append(rna_transferencia("".join(sequencia_rna[idx:idx+3])))
    # return aminoacidos
    return [
        amino_acid for batch in batched(rna_mensageiro(sequencia_dna), 3)
        if (amino_acid := rna_transferencia(''.join(batch)))
    ]
