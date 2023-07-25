"""
Dado uma coleção de intervalos, mesclar quaisquer intervalos que se sobreponham.
Escreva uma função que recebe uma lista de tuplas, onde cada tupla contém dois números
inteiros representando o início e o fim de um intervalo. 

Exemplo: 
Entrada: [(1, 3), (2, 6), (8, 10), (15, 18)] 
Saída: [(1, 6), (8, 10), (15, 18)] 



>>> mescla((1, 3), (2, 6))
(1, 6)
>>> mescla((1, 3), (2, 10))
(1, 10)





>>> intersec((1,3), (2,6))
True

>>> intersec((5,6), (7,8))
False

>>> intersec((5, 5), (6, 6))
False

>>> ordena_entrada([(1, 3), (2, 6), (15, 18), (8, 10)])
[(1, 3), (2, 6), (8, 10), (15, 18)]

>>> ordena_entrada([(1, 3), (8, 10), (2, 6)])
[(1, 3), (2, 6), (8, 10)]

>>> resolve([(1, 3), (2, 6), (8, 10), (15, 18)] )
[(1, 6), (8, 10), (15, 18)]
>>> resolve([(1, 3), (2, 6), (8, 10)])
[(1, 6), (8, 10)]

>>> resolve([(1, 3), (2, 6), (8, 10), (9, 50)])
[(1, 6), (8, 50)]

>>> resolve([(1, 3), (9, 50)])
[(1, 3), (9, 50)]

>>> resolve([(9, 50), (1, 3)])
[(1, 3), (9, 50)]

>>> resolve([(9, 50)])
[(9, 50)]
"""
def mescla(tp1, tp2):
   return (tp1[0], tp2[1])
      


def intersec(tp1, tp2):
    return tp2[0] < tp1[1]


def ordena_entrada(lista_de_tuplas):
   return sorted(lista_de_tuplas)

def resolve(lista_tuple):
    lista_orde = ordena_entrada(lista_tuple)
    resp = []
    i = 0
    while i < len(lista_orde):
        tp = lista_orde[i]
        for j in range(i + 1, len(lista_orde)): 
            if intersec(tp,lista_orde[j]):
                tp = mescla(tp,lista_orde[j])
                i += 1
            else:    
                break
        i += 1
        resp.append(tp) 
    
    return resp