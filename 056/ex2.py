"""
Um endereço IPv4 é representado como quatro números decimais separados por pontos.
Cada número deve estar no intervalo de 0 a 255.
Por exemplo, 192.168.0.1 é um endereço IPv4 válido, enquanto 256.100.50.0 não é.

A função deve receber uma string e retornar uma tupla.
O primeiro elemento da tupla deve ser um booleano (True se a string for um endereço
IPv4 válido, False caso contrário).
O segundo elemento deve ser uma mensagem de erro detalhando o motivo da falha,
ou None se for válido.

"192.168.0.1" -> (True, None)
"256.100.50.0" -> (False, "Um ou mais octetos estão fora do intervalo de 0 a 255")
"192.168.0" -> (False, "Formato incorreto, deve ter exatamente 4 octetos")
"192.168.0.abc" -> (False, "Um ou mais octetos não são números inteiros")

>>> is_ipv4("192.168.0.1")
True

>>> is_ipv4("192.168.0")
False

>>> is_ipv4("192.168.0.abc")
False

>>> is_ipv4("192.168.999.999")
False

>>> error("192.168.999.999")
'Um ou mais octetos estão fora do intervalo de 0 a 255'

>>> error("192.168.0")
'Formato incorreto, deve ter exatamente 4 octetos'

>>> error("192.168.0.abc")
'Um ou mais octetos não são números inteiros'

>>> error("192.168.0.1")
''

>>> resultado("192.168.0.1")
(True, None)

>>> resultado("192.168.0")
(False, 'Formato incorreto, deve ter exatamente 4 octetos')

>>> resultado("192.168.0.abc")
(False, 'Um ou mais octetos não são números inteiros')


"""

def is_ipv4(ip):
    valores = ip.split(".")
    if len(valores) != 4:
        return False
    for valor in valores:
        if not valor.isnumeric():
            return False
        if not (0 <= int(valor) <= 255):
            return False
    return True

def error(ip):
    valores = ip.split(".")
    if len(valores) != 4:
        return "Formato incorreto, deve ter exatamente 4 octetos"
    for valor in valores:
        if not valor.isnumeric():
            return "Um ou mais octetos não são números inteiros"
        if not (0 <= int(valor) <= 255):
            return "Um ou mais octetos estão fora do intervalo de 0 a 255"
    return ''

def resultado(ip):
    return (is_ipv4(ip), error(ip) if error(ip) else None)