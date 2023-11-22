"""
Agrupar anagramas:
Dado uma lista de strings, crie sublistas com as palavras que são anagramas.
Ordene as palavras em ordem alfabética.

Entrada:
["alergia", "muro", "corte", "rumo", "perda", "padre", "alegria", "pedra"]

Saída:
[["alegria", "alergia"], ["corte"], ["muro", "rumo"], ["padre", "pedra", "perda"]]


>>> eh_anagrama("alegria", "alergia")
True

>>> eh_anagrama("alegria", "muro")
False

>>> eh_anagrama("alegria", "alegriaa")
False

>>> agrupar_anagramas(["alergia", "muro", "corte", "rumo", "perda", "padre", "alegria", "pedra"])
[['alegria', 'alergia'], ['corte'], ['muro', 'rumo'], ['padre', 'pedra', 'perda']]

"""

def eh_anagrama(string1, string2):
    return sorted(string1) == sorted(string2)


def agrupar_anagramas(strings):
    new_string = []
    for i in range(len(strings)):
        new_string.append((strings[i], ''.join(sorted(strings[i]))))

    new_string = sorted(new_string, key= lambda x:x[1])
    
    print(new_string)
    aux = []
    aux2 = []

    for i in range(len(new_string)):
        print('H1 ', new_string[i][1])
        if(i == len(new_string) or i + 1 == len(new_string)  ):
            aux.append(new_string[i][0])
            aux2.append(aux)
            break

        if new_string[i][1] == new_string[i + 1][1]:
            aux.append(new_string[i][0])
        else:
            aux.append(new_string[i][0])
            aux2.append(aux)
            aux = []
    

    aux2 = sorted(aux2)
    print('func ', aux2)


    

    

    
    #while(i<len(strings) - 1): 
 
    # while len(strings) > 0:
    #     aux_string.append(strings[0])
    #     k =  1
 
        # while k < len(strings) -1:
        #     if eh_anagrama(strings[i][0], strings[k][0]):
        #         aux_string.append(strings[k])
        #         strings.pop(k)
        #     else:
        #         k += 1
        # new_string.append(aux_string)
        # aux_string = []
        # i+=1

    return aux2


