"""
Calculadora Polonesa Reversa

Implemente uma calculadora que utilize a notação polonesa reversa (RPN).
A calculadora deve suportar as operações básicas de adição (+), subtração (-),
multiplicação (*) e divisão (/). A entrada será uma string contendo os números e operadores
separados por espaços, e a saída deve ser o resultado da operação. Caso a entrada não seja válida,
retornar `None`.

Entrada: "2 3 +"
Saída: 5

Entrada: "4 5 * 3 -"
Saída: 17

Entrada: "3 *"
Saída: None

>>> op('1', '1', '+' )
'2'

>>> op('1', '3', '+' )
'4'

>>> op('2', '2', '-' )
'0'

>>> op('2', '2', '/' )
'1'

>>> op('2', '2', '*' )
'4'

>>> extraioperacao('2  2  *')
[['2'], ['2', '*']]

>>> extraioperacao('2  1  *')
[['2'], ['1', '*']]

>>> extraioperacao('2  1  * 2 -')
[['2'], ['1', '*'], ['2', '-']]

>>> extraioperacao('2')


>>> extraioperacao('2 2 - 2')

>>> calc('2 2 + 2 +')
'6'

>>> calc('2 2 + 3 +')
'7'

>>> calc('2 2')


>>> calc('2 2 + 2 - 2 / 7 *')
'7'
"""

def op(op1, op2, opp):
    val1 = int(op1)
    val2 = int(op2)

    if opp == '+':
        res = val1 + val2
    elif opp == '-':
        res = val1 - val2
    elif opp == '*':
        res = val1 * val2
    elif opp == '/':
        res = val1 // val2
    return str(res)


def extraioperacao(entrada):
    valores = entrada.split()
    if len(valores) < 3 or len(valores) % 2 == 0:
        return None

    res = []

    res.append([valores.pop(0)])

    while valores:
        res.append([valores.pop(0), valores.pop(0)])

    return res

def calc(entrada):
    valores = extraioperacao(entrada)

    if valores is None:
        return None
        
    op1 = valores.pop(0)[0]
    for valor in valores:
        op2 = valor[0]
        operador = valor[1]
        op1 = op(op1, op2, operador)
    
    return op1

