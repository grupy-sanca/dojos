"""
>>> goodfairy("Ruby and Crystal")
{'ruby': 3, 'crystal': 2}
>>> evilfairy("Python and Squirrel")
{'python': 2, 'squirrel': 2}
"""


def diamonds_and_toads(phrase, fairytype):
    if fairytype == "good":
        return goodfairy(phrase)
    elif fairytype == "evil":
        return evilfairy(phrase)


def goodfairy(phrase):
    crystals = phrase.count('c') + (2*phrase.count('C'))
    rubys = phrase.count('r') + (2*phrase.count('R'))
    return {"ruby": rubys, "crystal": crystals}


def evilfairy(phrase):
    pythons = phrase.count('p') + (2*phrase.count('P'))
    squirrels = phrase.count('s') + (2*phrase.count('S'))
    return {"squirrel": squirrels, "python": pythons}
