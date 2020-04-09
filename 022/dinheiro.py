"""
Dado um valor em reais (numérico), converter para a forma escrita
Por exemplo:
1 -> um real
100.5 -> cem reais e cinquenta centavos
20.35 -> vinte reais e trinta e cinco centavos

>>> numero_1_9(1)
'um'
>>> numero_1_9(2)
'dois'
>>> numero_10_19(13)
'treze'
>>> numero_20_90(20)
'vinte'
>>> numero_100(100)
'cem'
>>> concatena_moeda(1)
'um real'
>>> concatena_moeda(2)
'dois reais'
>>> concatena_moeda(10)
'dez reais'
>>> concatena_moeda(20)
'vinte reais'
>>> concatena_moeda(100)
'cem reais'
>>> concatena_moeda(66)
'sessenta e seis reais'
>>> concatena_moeda(66.10)
'sessenta e seis reais e dez centavos'
"""

def numero_1_9(numero):
    numeros_em_texto = {1: "um", 2: "dois", 3: "três", 4: "quatro",
                        5: "cinco", 6: "seis", 7: "sete", 8: "oito",
                        9: "nove"}
    return numeros_em_texto[numero]


def numero_10_19(numero):
    numeros_em_texto = {10: "dez", 11: "onze", 12: "doze", 13: "treze",
                        14: "quatorze", 15: "quinze", 16: "dezesseis",
                        17:"dezessete", 18: "dezoito",  19: "dezenove"}
    return numeros_em_texto[numero]

def numero_20_90(numero):
    numeros_em_texto = {20: "vinte", 30: "trinta", 40: "quarenta",
                        50: "cinquenta", 60: "sessenta", 70: "setenta",
                        80:"oitenta", 90: "noventa"}
    return numeros_em_texto[numero]

def numero_100(numero):
    return "cem"

def concatena_moeda(numero):
    if numero == 1:
        return numero_1_9(numero) + " real"
    else:
        if 1 <= numero <= 9:
            return numero_1_9(numero) + " reais"
        elif 10 <= numero <= 19:
            return numero_10_19(numero) + " reais"
        elif 20 <= numero <= 90:
            numero_str = str(numero)
            centavos = 0
            if "." in numero_str:
                real, centavos = numero_str.split(".")
            else:
                real = numero_str
            dezena = real[0] + "0"
            unidade = real[1]
            dezena_centavo = centavos[0] + "0"
            unidade_centavo = centavos[1]
            if unidade == "0":
                real_extenso = numero_20_90(numero) + " reais"
            else:
                real_extenso = numero_20_90(int(dezena)) + " e " + numero_1_9(int(unidade)) + " reais"
            if int(centavos) == 0:
                return real_extenso
            else:
                return real_extenso + " e " + numero_10_19(int(dezena_centavo)) " centavos"
        else:
            return numero_100(numero) + " reais"