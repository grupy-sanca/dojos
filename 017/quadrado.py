"""
Validador de quadrados mágicos (https://www.codewars.com/kata/57be6a612eaf7cc3af000178)

>>> linha = [1, 2, 3]
>>> valida_vetor(linha)
False
>>> valida_vetor([4, 5, 6])
True
>>> matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> valida(matriz)
False
>>> matriz = [[1, 2, 3], [4, 5, 6], [4, 5, 6]]
>>> valida(matriz)
False
>>> matriz = [[4, 5, 6], [4, 5, 6], [4, 5, 6]]
>>> é_mágica([[4, 5, 6], [4, 5, 6], [4, 5]])
False
>>> matriz = [[4,5,6]]
>>> é_mágica(matriz)
False
>>> é_mágica([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
False
>>> é_mágica([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
True
>>> é_mágica([[1, 2, 3], [4, 4, 6], [7, 8, 9]])
False
>>> é_mágica([[1, 2, 3], [4, 4, 6], [7, 8, 9], [2, 2, 4]])
False
>>> é_mágica([[1, 2, 3], [10, 4, 6], [7, 8, 9]])
False
>>> é_mágica([[Exception, 2, 3], [1, 4, 6], [7, 8, 9]])
False
>>> valida([[1, 2, 3], [4, 4, 6], [7, 8, 9], [2, 2, 4]])
False
>>> valida([[4, 5, 6], [4, 5, 6], [4, 5, 6], [4, 5, 6]])
False
>>> valida([[4, 5, 6], [4, 5, 6], [4, 5, 6]])
False
>>> valida([[4, 5, 6], [1, 2, 3], [7, 8, 9]])
False
>>> valida([[4, 9, 2], [3, 5, 7], [8, 1, 6]])
True
>>> valida([[4, 2, 9], [3, 5, 7], [8, 1, 6]])
False
>>> valida([[3, 5, 7],[4, 9, 2], [8, 1, 6]])
False
>>> valida([[2, 7, 6],[9, 5, 1],[4, 3, 8]])
True
"""

def é_mágica(matriz):
    gabarito = list(range(1, 10))
    for linha in matriz:
        for num in linha:
            try:
                gabarito.remove(num)
            except ValueError:
                return False
        if len(linha) != 3:
            return False
    return len(matriz)==3

def valida(matriz):
    if not é_mágica(matriz):
        return False
    é_valida = True
    sum = [ 0, 0, 0]
    for linha in matriz:
        é_valida = valida_vetor(linha)
        if not é_valida:
            return é_valida
        sum[0] += linha[0]
        sum[1] += linha[1]
        sum[2] += linha[2]
    if(sum[0] != 15 or sum[1] != 15 or sum[2] != 15):
        return False

    if matriz[0][0] + matriz[1][1] + matriz[2][2] != 15:
        return False
    if matriz[0][2] + matriz[1][1] + matriz[2][0] != 15:
        return False
    return True

def valida_vetor(linha):
    return sum(linha) == 15
