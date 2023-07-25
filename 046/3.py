"""
Escreva uma função que gere todos os números primos até n.
Um número primo é um número natural maior que 1 que não possui divisores
positivos além de 1 e ele mesmo.

Exemplo:
Entrada: 10
Saída: [2, 3, 5, 7]

Exemplo adicional:
Entrada: 20
Saída: [2, 3, 5, 7, 11, 13, 17, 19]

>>> is_primo(5)
True

>>> is_primo(10)
False

>>> is_primo(16)
False

>>> is_primo(2358)
False

>>> escreve_primo(10)
[2, 3, 5, 7]

>>> escreve_primo(19)
[2, 3, 5, 7, 11, 13, 17, 19]
"""

def is_primo(n):
    for i in range(2, int(n**(0.5)+1)):
        if n % i == 0:
            return False
    return True

def escreve_primo(n):
    lista_result =[]
    for i in range(2, n+1):
        if (is_primo(i)):
            lista_result.append(i) 

    
    return lista_result
