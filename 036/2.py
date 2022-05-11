"""
https://www.codewars.com/kata/515decfd9dcfc23bb6000006

>>> eh_ip("0.0.0.0")
True

>>> eh_ip("600.0.0.0")
False

>>> eh_ip("0.0.0")
False

>>> eh_ip("0,0,0,0")
False

>>> eh_ip("a.b.c.d")
False

>>> eh_ip("0.a.b.c")
False
"""

def eh_ip(ip):
    ip_lista = ip.split(".")
    if len(ip_lista) != 4:
        return False

    for n in ip_lista:
        try:
            n = int(n)
        except Exception:
            return False
        if n < 0 or n > 255:
            return False
    return True
