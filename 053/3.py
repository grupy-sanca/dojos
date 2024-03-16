"""
3 - Ao codificar uma palavra, ela agora será composta de valores numéricos.
Esses valores numéricos podem ser somados, resultando no "valor bruto da palavra".
Entretanto, palavras longas tem a tendência de terem um valor maior, pois possuem mais letras,
e consequentemente mais números. Para equilibrar isso, podemos extrair o "valor médio da palavra",
que é o valor bruto da palavra dividido pela quantidade de letras que essa palavra tem.

Crie uma função que receba uma frase e retorne dois resultados:
a palavra decodificada que possui o maior valor médio, e o seu valor médio.

Exemplo: valor_medio("dojo python") --> ("python", 5.33)

A resposta acima usa o exemplo de decodificação do exercício 2, onde PYTHON,
palavra de 6 letras, é codificada como 4 5 6 7 2 8, cuja soma é 32, e 32/6 = 5.33


>>> encode_letter("A")
1

>>> encode_letter("B")
2

>>> encode_word("DOJO")
'4 15 10 15'

>>> encode_word("DOJO PY")
'4 15 10 15 27 16 25'

>>> encode_word("dojo")
'31 42 37 42'

>>> pegar_valor_palavra("DOJO")
11.0

>>> pegar_valor_palavra("PY")
20.5

>>> pega_valor_frase("DOJO PY")
('PY', 20.5)

>>> pega_valor_frase("DOJO")
('DOJO', 11.0)
"""
from string import ascii_uppercase, ascii_lowercase


def encode_letter(letter: str) -> int:
    mapping = {char: number + 1 for number, char in enumerate(ascii_uppercase + " " + ascii_lowercase)}
    return mapping.get(letter)


def encode_word(word: str):
    return " ".join([str(encode_letter(letter)) for letter in word])


def pegar_valor_palavra(palavra):
    palavra_encodada = encode_word(palavra)
    return sum([int(number) for number in palavra_encodada.split(" ")])/len(palavra)


def pega_valor_frase(frase):
    return max([(palavra, pegar_valor_palavra(palavra)) for palavra in frase.split(" ")]) 
