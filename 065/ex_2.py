"""
O Cadastro de Pessoa Física, ou CPF brasileiro, é um documento cujo número pode ser validado por um algoritmo.
Para validar um CPF, precisamos verificar se seus dois dígitos verificadores estão em conformidade
com os outros 9 primeiros dígitos.
Para validar o primeiro dígito verificador, pegamos os 9 primeiros dígitos e multiplicamos cada um,
da direita para a esquerda, por números crescentes à partir do 2. Ao fim, soma-se todos os valores obtidos.

Por exemplo, para o CPF 11144477735, a combinação seria:
1  1 1 4 4 4 7 7 7
10 9 8 7 6 5 4 3 2
1*10 + 1*9 + 1*8 + 4*7 + 4*6 + 4*5 + 7*4 + 7*3 + 7*2 = 162

Deste resultado, pegamos o resto da divisão por 11: 162 / 11 = 14 com resto 8

Por fim, fazemos uma última verificação:
- Se o resto é menor que 2, o dígito verificador é 0
- Se o resto é 2 ou mais, o dígito verificador é o resultado de 11 menos o resto da divisão: 11 - 8 = 3

Para validar o segundo dígito, o processo é repedido, porém, agora,
junta-se o primeiro dígito validador aos 9 primeiros dígitos, e a lista de números
crescentes para multiplicação vai de 2 até 11.

1  1  1 4 4 4 7 7 7 3
11 10 9 8 7 6 5 4 3 2
1*11 + 1*10 + 1*9 + 4*8 + 4*7 + 4*6 + 7*5 + 7*4 + 7*3 + 3*2 = 204

O resto da divisão: 204 / 11 = 18 com resto 6

E para a última verificação, 6 não é menor que 2, portanto o segundo dígito verificador é 11 - 6 = 5

O CPF que começa com 111444777 deve ter como dígitos verificadores '35'.
Como esse foi o CPF indicado, ele é um CPF válido.

Vamos criar um validador para CPF que recebe uma string contendo um CPF e retorna se ele é válido ou não.

validador_cpf('11144477735')
True

validador_cpf('11144477767')
False

>>> validador_cpf('11144477735')
True

>>> validador_cpf('11144477767')
False

>>> gera_soma_produto('111444777')
162

>>> get_digito(162)
'3'

>>> get_digito(204)
'5'

>>> gera_digitos('111444777')
'35'
"""


def gera_soma_produto(cpf_parcial):
    passo1 = zip([int(item) for item in cpf_parcial], range(len(cpf_parcial) + 1, 1, -1))
    product_list = [item1*item2 for item1, item2 in passo1]
    return sum(product_list)


def get_digito(soma):
    resto = soma % 11
    if resto < 2:
        return '0'
    return str(11 - resto)


def gera_digitos(cpf):
    primeiro_digito = get_digito(gera_soma_produto(cpf))
    segundo_digito = get_digito(gera_soma_produto(cpf + primeiro_digito))

    return f'{primeiro_digito}{segundo_digito}'


def validador_cpf(cpf):
    cpf_root = cpf[:9]
    validation_digits = cpf[9:]
    expected_digits = gera_digitos(cpf_root)
    return validation_digits == expected_digits
