"""
    Problema: https://www.hackerrank.com/challenges/python-time-delta/problem

    Exemplo de entrada:
    Sun 10 May 2015 13:54:36 -0700
    Sun 10 May 2015 13:54:36 -0000

    Sat 02 May 2015 19:54:36 +0530
    Fri 01 May 2015 13:54:36 -0000

    Exemplo de saída:
    25200 => 7 (horas) * 60 * 60 (converter para segundos)


>>> calcula_diferenca("Sun 10 May 2015 13:54:36 -0700","Sun 10 May 2015 13:54:36 -0000")
25200

>>> calcula_diferenca("Sat 02 May 2015 19:54:36 +0530","Fri 01 May 2015 13:54:36 -0000")
88200
"""

import datetime

def calcula_diferenca(timestamp_antes,timestamp_depois):
    date_format = "%a %d %b %Y %H:%M:%S %z"
    date_object_antes = datetime.datetime.strptime(timestamp_antes, date_format)
    date_object_depois = datetime.datetime.strptime(timestamp_depois,date_format)
    diferenca = date_object_depois - date_object_antes
    
    return abs(int(diferenca.total_seconds()))
