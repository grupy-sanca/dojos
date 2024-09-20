"""
4 - Texas Hold'em é uma variante de Poker na qual cada jogador recebe duas "cartas fechadas". 
Os jogadores então fazem uma série de apostas enquanto cinco "cartas comunitárias" são distribuídas. 
Se houver mais de um jogador restante quando as apostas param, ocorre uma "revelação", na qual os jogadores mostram suas cartas. 
Cada jogador faz a melhor mão de poker possível usando cinco das sete cartas disponíveis (cartas comunitárias + as cartas fechadas
 do jogador).

As mãos possíveis são, em ordem decrescente de valor:

* Sequência de cores (cinco cartas consecutivas do mesmo naipe). Maior valor é melhor.
* Quadra (quatro cartas com o mesmo valor). O desempate é primeiro pelo valor, depois pelo valor da carta restante.
* Full house (três cartas com o mesmo valor, duas com outro). O desempate é primeiro pelo valor das três cartas, 
depois pelo valor do par.
* Flush (cinco cartas do mesmo naipe). Valores mais altos são melhores, comparados de maior para menor valor.
* Sequência (cinco cartas consecutivas). Maior valor é melhor.
* Trinca (três cartas com o mesmo valor). O desempate é primeiro pelo valor das três cartas, depois pelo maior valor restante, 
depois pelo segundo maior valor restante.
* Dois pares (duas cartas com o mesmo valor, duas cartas com outro valor). O desempate é primeiro pelo valor do par mais alto, 
depois pelo valor do par mais baixo e depois pelo valor da carta restante.
* Par (duas cartas com o mesmo valor). O desempate é primeiro pelo valor das duas cartas, depois pelos três valores restantes.
* Nada.

O desempate é o valor das cartas de maior para menor valor.
Dadas as cartas fechadas e as cartas comunitárias, complete a função para retornar o tipo de mão e uma lista de valores em 
ordem decrescente de significância, para usar na comparação contra outras mãos do mesmo tipo, da melhor mão possível.

Exemplos:
Entrada: ["A♠️", "A♦️"], ["J♣️", "5♥️", "10♥️", "2♥️", "3♦️"]
Saída: {"tipo": "par", "valores: ["A", "J", "10", "5"]}

Entrada: ["A♠️", "K♦️"], ["J♥️", "5♥️", "10♥️", "Q♥️", "3♥️"]
Saída: {"tipo": "flush", "valores": ["Q", "J", "10", "5", "3"]}

>>> separa_naipe_numero(["2♠️", "3♠️", "4♠️"])
{'2': '♠️', '3': '♠️', '4': '♠️'}

>>> checa_sequencia_com_naipe(["2♠️", "3♠️", "4♠️", "5♠️", "6♠️", "2♥️", "3♦️"])
True

 checa_sequencia_com_naipe(["5♠️", "3♠️", "4♠️", "5♠️", "6♠️", "2♥️", "3♦️"])
False
"""


def separa_naipe_numero(cartas: list[str])->dict:
    dicionario = {}
    for carta in cartas:
        chave_num = carta[0]
        valor_naipe = carta[1]
        dicionario[chave_num] = valor_naipe
    return dicionario


def checa_sequencia_com_naipe(cartas):
    return True
