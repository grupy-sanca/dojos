"""
3 - O fazendeiro Eustáquio tem uma fazenda muito grande, onde ele cria galinhas, porcos e vacas.
É muito difícil contar todos os animais da fazenda, e por isso Eustáquio comprou um sistema que faz isso por ele.
Porém, Eustáquio comprou um sistema muito ruim, pois ao invés de contar os animais, ele conta o número de patas, de cabeças e de chifres.
Corrija esse sistema e ajude Eustáquio a saber quantos animais têm em sua fazenda.

Crie uma função que receba o número de patas, cabeças e chifres e retorne o número de galinhas, porcos e vacas.
contar_animais(patas: int, cabecas: int, chifres: int) -> dict

Observação: todas as galinhas possuem 2 patas, 1 cabeça e 0 chifres. Todos os porcos possuem 4 patas, 1 cabeça e 0 chifres. Todas as vacas possuem 4 patas, 1 cabeça e 2 chifres.

Exemplos:
contar_animais(34, 11, 6)
{'galinhas': 5, 'porcos': 3, 'vacas': 3}

contar_animais(154, 42, 10)
{'galinhas': 7, 'porcos': 30, 'vacas': 5}

>>> contar_vacas(6)
3

>>> contar_vacas(10)
5

>>> decompoe_vacas(10)
(40, 10)

>>> decompoe_vacas(5)
(20, 5)

>>> contar_animais(34, 11, 6)
{'galinhas': 5, 'porcos': 3, 'vacas': 3}

>>> contar_animais(154, 42, 10)
{'galinhas': 7, 'porcos': 30, 'vacas': 5}

"""


def contar_animais(nro_patas, nro_cabecas, nro_chifres):
    vacas = contar_vacas(nro_chifres)
    patas_vacas, cabecas_vacas = decompoe_vacas(vacas)
    nro_patas -= patas_vacas
    nro_cabecas -= cabecas_vacas

    porcos = (nro_patas - 2*nro_cabecas) //  2
    galinhas = nro_cabecas - porcos
    return {'galinhas': galinhas, 'porcos': porcos, 'vacas': vacas}


def contar_vacas(nro_chifres):
    return nro_chifres // 2


def decompoe_vacas(nro_vacas):
    return 4*nro_vacas, nro_vacas
