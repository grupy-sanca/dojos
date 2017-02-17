"""
Problema pego do URI:
https://www.urionlinejudge.com.br/judge/en/problems/view/1667

>>> br_to_newline('<br>')
'\\n'
>>> br_to_newline('casa <br> rua')
'casa \\n rua'
>>> br_to_newline('casa <<br>> rua')
'casa <\\n> rua'
>>> br_to_newline('<br> hue <br> hue <br> hue')
'\\n hue \\n hue \\n hue'
>>> hr_to_dashed_line('\\n<hr>')
'\\n---\\n'
>>> hr_to_dashed_line('<hr>')
'\\n---\\n'
>>> hr_to_dashed_line('<hr> hue <hr> hue <hr> hue')
'\\n---\\n hue \\n---\\n hue \\n---\\n hue'

"""


def br_to_newline(bla):
    return bla.replace('<br>', '\n')


def hr_to_dashed_line(bla):
    return bla.replace('\n<hr>', '\n---\n').replace('<hr>', '\n---\n')


