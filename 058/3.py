"""
Soma de Subconjunto

Escreva uma função que determine se existe um subconjunto de uma lista de números inteiros
que some exatamente a um valor alvo. O subconjunto pode conter zero ou mais elementos da lista original.
Sua função deve retornar `True` se existir tal subconjunto e `False` caso contrário.

Parâmetros:
- `nums`: Uma lista de números inteiros. Pode conter números positivos e negativos.
- `alvo`: Um número inteiro que representa o valor alvo que o subconjunto deve somar.

Entrada: ([2, 3, 7, 8, 10], 11)
   Saída: True
   Explicação: O subconjunto `[3, 8, 10]` soma 11.

Entrada: ([1, 2, 5, 6], 11)
   Saída: True
   Explicação: O subconjunto `[5, 6]` soma 11.

Entrada: ([1, 2, 3], 7)
   Saída: False
"""