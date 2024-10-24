"""
1) Dado um número inteiro n_coluna, retorne o título da coluna correspondente como aparece em uma planilha do Excel.

Por exemplo:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...

Exemplo 1:
Entrada: n_coluna = 1
Saída: "A"

Exemplo 2:
Entrada: n_coluna = 28
Saída: "AB"

Exemplo 3:
Entrada: n_coluna = 701
Saída: "ZY"

>>> Converte_Coluna(1)
'A'

>>> Converte_Coluna(2)
'B'

>>> Converte_Coluna(28)
'AB'

>>> Converte_Coluna(701)
'ZY'

>>> Converte_Coluna(26)
'Z'

>>> Converte_Coluna(703)
'AAA'
"""
def Converte_Coluna(n_coluna):
    if n_coluna <= 26:
        if n_coluna == 26:
            return 'Z'
        return chr(n_coluna + ord('A') - 1)
    return Converte_Coluna(n_coluna // 26) + Converte_Coluna(n_coluna % 26)
