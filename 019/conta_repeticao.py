'''

Remover repetições (https://imgur.com/a/yRjKi62)

>>> conta_repeticoes([1, 2, 1])
{1: 2, 2: 1}

>>> conta_repeticoes([1])
{1: 1}

>>> imprime_repeticoes([1, 2, 1])
1 2

>>> imprime_repeticoes([10, 2, 1, 2, 10])
2 2
10 2

>>> imprime_repeticoes([10, 2, 1, 3])

>>> imprime_repeticoes([10, 2, 1, 2, 10, 3, 3, 3])
2 2
3 3
10 2

'''

def conta_repeticoes(lista):
	contagem = {}
	for num in lista:
		contagem[num] = contagem.get(num, 0) + 1
	return contagem

def imprime_repeticoes(lista):
	contagem = conta_repeticoes(lista)

	final = (
		(num, quantidade) 
		for num, quantidade in contagem.items()
		if quantidade > 1
	)

	# for num, quantidade in contagem.items():
	# 	if quantidade > 1:
	# 		final.append((num, quantidade))

	for par in sorted(final):
		print(par[0], par[1])
