"""
https://www.hackerrank.com/challenges/staircase/problem

>>> escadinha(4)
   #
  ##
 ###
####
>>> escadinha(5)
    #
   ##
  ###
 ####
#####
"""


def escadinha(n):
    for i in range(1, n + 1):
        cerquilha = '#' * i
        print(cerquilha.rjust(n))  # str.rjust adiciona n espaços à esquerda de str
