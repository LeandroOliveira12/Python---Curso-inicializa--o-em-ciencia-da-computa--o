#Dado número inteiro n, sendo que n é maior que 1,
#positivo maior que 1 imprimir a sua decomposição fatores primos indicando também a multiplicidade de cada fator.
import math
    
def debug_div(div,cont,armazena,resto, entrada):
    print ("Dividindo por: ",div)
    print ("Quantidade:",cont)
    print("Armazena Div: ",armazena)
    print ("resto:",resto)
    print("Valor entrada: ", entrada)
    return


    

def Fator_primo ():
    cont_div_2 = 0
    resto_div_2 = 1
    armazena_div_2 = 0
    key_div_2 = False



    cont_div_3 = 0
    resto_div_3 = 1
    armazena_div_3 = 0
    key_div_3 = False

    cont_div_5 = 0
    resto_div_5 = 1
    armazena_div_5 = 0
    key_div_5 = False

    key_passage = True



    print("Programa que decompoe os Fatores Primos, e indica da multiplicidade de cada fator")
    entrada = int(input("Digite um número inteiro positivo: "))

######################## Divisão por 2 ##############################
    resto_div_2 = entrada %2
    
    if resto_div_2 == 0:
        key_div_2 = True
    else:
        key_div_2 = False

        
    while key_div_2 == True:
        
        cont_div_2+= 1
        armazena_div_2 = entrada/2           
        resto_div_2 = armazena_div_2 % 2        
        entrada = armazena_div_2
        
        #debug_div(2,cont_div_2,armazena_div_2,resto_div_2,entrada)
           
        if resto_div_2 == 0:
            key_div_2 == True
        else:
            key_div_2 = False

######################## Divisão por 3 ##############################
            
    resto_div_3 = entrada %3
    
    if resto_div_3 == 0:
        key_div_3 = True
    else:
        key_div_3 = False

        
    while key_div_3 == True:
        
        cont_div_3+= 1
        armazena_div_3 = entrada/3           
        resto_div_3 = armazena_div_3 % 3        
        entrada = armazena_div_3
        
        #debug_div(3,cont_div_3,armazena_div_3,resto_div_3,entrada)
           
        if resto_div_3 == 0:
            key_div_3 == True
        else:
            key_div_3 = False

        

######################## Divisão por 5 ##############################
    resto_div_5 = entrada %5
    
    if resto_div_5 == 0:
        key_div_5 = True
    else:
        key_div_5 = False

        
    while key_div_5 == True:
        
        cont_div_5+= 1
        armazena_div_5 = entrada/5           
        resto_div_5 = armazena_div_5 % 5
        entrada = armazena_div_5
        
        #debug_div(5,cont_div_5,armazena_div_5,resto_div_5,entrada)
        
        
        if resto_div_5 == 0:
            key_div_5 == True
        else:
            key_div_5 = False

######################## Validando Entrada ##############################
    valida_entrada = 1
    
    if   cont_div_2 > 0:
        valida_entrada = valida_entrada * math.pow(2,cont_div_2)
    if   cont_div_3 > 0:
        valida_entrada = valida_entrada * math.pow(3,cont_div_3)
    if   cont_div_5 > 0:
        valida_entrada = valida_entrada * math.pow(5,cont_div_5)
        




            


    return print ("Valor de entrada = ", int(valida_entrada))
    
