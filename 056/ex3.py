"""
Um endereço IPv6 é representado como oito grupos de quatro dígitos hexadecimais
separados por dois pontos. Os dígitos podem incluir números de 0 a 9 e letras de
A a F (maiúsculas ou minúsculas).
Por exemplo, 2001:0db8:85a3:0000:0000:8a2e:0370:7334 é um endereço IPv6 válido,
enquanto 2001:db8:85a3::8a2e:370g:7334 não é.

A função deve receber uma string e retornar uma tupla. O primeiro elemento da
tupla deve ser um booleano (True se a string for um endereço IPv6 válido, False
caso contrário).
O segundo elemento deve ser uma mensagem de erro detalhando o motivo da falha,
ou None se for válido.

"2001:0db8:85a3:0000:0000:8a2e:0370:7334" -> (True, None)
"2001:db8:85a3:0:0:8a2e:370g:7334" -> (False, "Um ou mais grupos contêm caracteres inválidos")
"2001:0db8:85a3" -> (False, "Formato incorreto, deve ter exatamente 8 grupos")


>>> erro("2001:db8:85a3:0:0:8a2e:370a:7334")

>>> erro("2001:db8:85a3:0:0:8a2g:370a:7334")
'Um ou mais grupos contêm caracteres inválidos'

>>> erro("2001:0db8:85a3")
'Formato incorreto, deve ter exatamente 8 grupos'

>>> is_ipv6("2001:db8:85a3:0:0:8a2e:370a:7334")
(True, None)

>>> is_ipv6("2001:db8:85a3:0:0:8a2g:370a:7334")
(False, 'Um ou mais grupos contêm caracteres inválidos')


>>> is_ipv6("2001:db8:85a3:0:0:8a2a:370a")
(False, 'Formato incorreto, deve ter exatamente 8 grupos')
"""

def erro(ip):
    if ip.count(":") != 7:
        return 'Formato incorreto, deve ter exatamente 8 grupos'
    validos = "0123456789abcdefABCDEF:"
    for valor in ip:
        if valor not in validos:
            return 'Um ou mais grupos contêm caracteres inválidos'
    return
    
def is_ipv6(ip):
    err = erro(ip)
    return (err is None, err)