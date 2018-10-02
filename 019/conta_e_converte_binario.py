'''
>>> converte_decimal('1')
1

>>> converte_decimal('1010')
10

>>> contar(['100'])
{'100': 1}

>>> contar(['1000', '100', '1010'])
{'1000': 1, '100': 1, '1010': 1}

>>> imprime_decimal(['100'])
1 4

>>> imprime_decimal(['1000', '100', '1010'])
1 8
1 4
1 10
'''

def converte_decimal(binario):
	num = 0
	for i, bit in enumerate(reversed(binario)):
		num += int(bit) * 2 ** i
	return num

def contar(lista):
	contagem = {}
	for num in lista:
		contagem[num] = contagem.get(num, 0) + 1
	return contagem

def imprime_decimal(lista):
	contagem = contar(lista)

	for binario, qnt in contagem.items():
		print(qnt, converte_decimal(binario) 	)