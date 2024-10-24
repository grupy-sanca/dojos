"""
2) Os numerais romanos são representados por sete símbolos diferentes: I, V, X, L, C, D e M.

Valores:
I -> 1
V -> 5
X -> 10
L -> 50
C -> 100
D -> 500
M -> 1000

Por exemplo, o número 2 é escrito como II em numeral romano, apenas dois "uns" somados.
O número 12 é escrito como XII, que é simplesmente X + II. O número 27 é escrito como XXVII, que é XX + V + II.

Os numerais romanos geralmente são escritos do maior para o menor, da esquerda para a direita.
No entanto, o numeral para quatro não é IIII. Em vez disso, o número quatro é escrito como IV.
Como o um está antes do cinco, subtraímos, resultando em quatro.
O mesmo princípio se aplica ao número nove, que é escrito como IX.

Existem seis casos em que a subtração é usada:
    I pode ser colocado antes de V (5) e X (10) para formar 4 e 9.
    X pode ser colocado antes de L (50) e C (100) para formar 40 e 90.
    C pode ser colocado antes de D (500) e M (1000) para formar 400 e 900.

Dado um numeral romano, converta-o para um número inteiro.

Exemplo 1:
Entrada: s = "III"
Saída: 3
Explicação: III = 3.

Exemplo 2:
Entrada: s = "LVIII"
Saída: 58
Explicação: L = 50, V = 5, III = 3.

Exemplo 3:
Entrada: s = "MCMXCIV"
Saída: 1994
Explicação: M = 1000, CM = 900, XC = 90 e IV = 4.

>>> converte_romano("I")
1

>>> converte_romano("V")
5

>>> converte_romano("IV")
4

>>> converte_romano("MCMXCIV")
1994

>>> converte_romano("LVIII")
58

"""
def converte_romano(n_romano):
    romanos = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    for idx, n in enumerate(n_romano):
        if idx < len(n_romano)-1 and romanos[n] < romanos[n_romano[idx+1]]:
            result -= romanos[n]
        else:
            result += romanos[n]
    return result
