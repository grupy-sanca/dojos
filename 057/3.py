"""
Validação de Expressões Matemáticas

Desenvolva uma função que valide se uma expressão matemática está correta em termos
de parênteses e operadores. A função deve retornar verdadeiro se a expressão estiver
correta e falso caso contrário. A expressão pode conter números inteiros, operadores (+, -, *, /),
parênteses de abertura e fechamento, e espaços em branco.

Após isso, implementar um resolvedor de expressões sem o uso do `eval`.

Exemplos:

Entrada: "((1 + 2) * (3 - 4))"
Saída: True

Entrada: "(1 + 2) * (3 - 4"
Saída: False

>>> op('1', '1', '+' )
'2'

>>> op('1', '2', '+' )
'3'

>>> valida_parenteses('(1 + 1)')
True

>>> valida_parenteses('(1 + 1))')
False


>>> valida_parenteses('()1 + 1))')
False

>>> valida_expressao('1 + 1')
True

>>> valida_expressao('1 + 1 -')
False
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

def valida_parenteses(entrada):
    lista = []
    for token in entrada:
        if token == '(':
            lista.append(token)
        elif token == ')':
            if len(lista) == 0:
                return False
            lista.pop()

    if lista:
        return False
    return True

def valida_expressao(entrada: str):
    op1 = ""
    op2 = ""
    operando = ""

    i = 0
    while i < len(entrada):
        token = entrada[i]

        if token.isnumeric():
            op1 += token

        


