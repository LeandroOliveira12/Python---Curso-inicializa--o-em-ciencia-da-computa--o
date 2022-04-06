#Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros,
#verifica se tal lista possui elementos repetidos e os remove.
#A função deve devolver uma lista correspondente à primeira lista,
#sem elementos repetidos. A lista devolvida deve estar ordenada.

def remove_repetidos(lista):
    lista_semRepet = lista[:]
    lista_semRepet = sorted(lista_semRepet)
    cont_fixo = 0
    cont_vari = 1
    #print(lista_semRepet)
    while cont_fixo < len(lista_semRepet):    
        while cont_vari < len(lista_semRepet):
            if lista_semRepet[cont_fixo] == lista_semRepet[cont_vari] and cont_vari != cont_fixo :
                del lista_semRepet[cont_vari]
            cont_vari+=1
        cont_fixo+=1
        cont_vari = 0
        #print(lista_semRepet)
    
    return lista_semRepet
    


#lista_semRepet = remove_repetidos(lista)
