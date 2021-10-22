"""
Exercício Digitador Gago
(https://www.urionlinejudge.com.br/judge/pt/problems/view/2815)

Francisco Iote é uma gago diferente.
Ele não somente fala repetindo sílabas como estranhamente quando digita um texto
ele repete algumas sílabas, tornando a leitura muito chata.
Ele repete apenas sílabas que tenham exatamente 2 letras e nunca repete uma sílaba
que não seja a primeira sílaba da palavra. Ele também repete apenas uma vez, ou seja
a palavra bola, por exemplo, pode aparecer como bola ou bobola, nunca bobobola.

Você foi chamado como perito para traduzir alguns textos excritos por Francisco
eliminando as redundâncias de texto por ele geradas.


* Exemplo de entrada:
Juca comprou fafarinha na memercearia e papagou 4 reais o quilo.
A mamae de Juca pediu para ele comprar mamais 2 quilos.

* Exemplo de saída:
Juca comprou farinha na mercearia e pagou 4 reais o quilo.
A mae de Juca pediu para ele comprar mais 2 quilos.

>>> desgagueijador('Juca comprou fafarinha na memercearia e papagou 4 reais o quilo. A mamae de Juca pediu para ele comprar mamais 2 quilos.')
'Juca comprou farinha na mercearia e pagou 4 reais o quilo. A mae de Juca pediu para ele comprar mais 2 quilos.'

>>> desgagueijador('O papassarinho vovoou para bem longe.')
'O passarinho voou para bem longe.'

>>> desgagueijador("Jujuca cocomprou")
'Juca comprou'
"""

def desgagueijador(texto):    
    return " ".join([corrige_gagueira(palavra) for palavra in texto.split(' ')])

def corrige_gagueira(palavra):
    if palavra[0:2].lower() == palavra[2:4].lower():
        return palavra[0:2] + palavra[4:]
  
    return palavra
