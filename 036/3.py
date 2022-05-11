"""
https://www.codewars.com/kata/5aceae374d9fd1266f0000f0

Given two times in hours, minutes, and seconds (ie '15:04:24'), add or subtract them. This is a 24 hour clock. Output should be two digits for all numbers: hours, minutes, seconds (ie '04:02:09').

>>> sum('00:00:00', '00:00:00')
'00:00:00'

>>> sum('01:02:03', '02:02:02')
'03:04:05'

>>> sum('00:40:00', '00:40:02')
'01:20:02'

>>> sum('23:40:59', '00:40:02')
'00:21:01'

>>> sub('03:04:05', '01:01:01')
'02:03:04'

>>> sub('00:04:05', '01:01:01')
'23:03:04'

>>> sub('00:00:00', '01:01:01')
'22:58:59'
"""

def sum(t1, t2):
    h1, m1, s1 = [int(i) for i in t1.split(':')]
    h2, m2, s2 = [int(i) for i in t2.split(':')]

    s = (s1 + s2)
    m = (m1 + m2)
    h = (h1 + h2)
    h = (h % 24 + (m//60)) % 24
    m = (m % 60 + (s//60)) % 60
    s = s % 60
    # 
    # 

    return f"{h:02d}:{m:02d}:{s:02d}"

def sub(t1,t2):
    h1, m1, s1 = [int(i) for i in t1.split(':')]
    h2, m2, s2 = [int(i) for i in t2.split(':')]

    h = h1 - h2
    m = m1 - m2
    s = s1 - s2

    h = (24 + h) % 24
    m = (60 + m - (s + 60)//60) % 60
    s = (60 + s) % 60


    return f"{h:02d}:{m:02d}:{s:02d}"
