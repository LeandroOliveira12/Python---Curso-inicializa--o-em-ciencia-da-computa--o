
num = int(input("Digite o numero: "))

####### Váriaveis rotina de comparadação de igualdade ##########
igualdade = False
atual = 0
anterior = 1
soma_compar = 0


####### Variavéis para criação da chave de finalização #########
entrada = num
key = 0
cont = 0
soma = 0
passagem = True


##############################################################


while cont < 10:
    soma = entrada % 10
    entrada = entrada // 10
    key = key + soma
    cont  = cont + 1
    print ("key:",key)


while igualdade == False and passagem == True:
  
    anterior = num % 10 #armazena 1° algarismo
    print ("anterior: ", anterior)
    num = num // 10 #descarta 1° algarismo
    
    soma_compar = anterior + soma_compar
    
    atual = num % 10 # armazena 2° algarismo
    print ("atual: ", atual)        
    print ("Comparação algarismo, Valor anterior:",anterior, "Valor Atual: ", atual,"Soma Comparacão:", soma_compar)

    

    if anterior != atual:
         print ("Os dois algarismo são diferentes, o anterior é:",anterior, " e o Atual é: ", atual)
    else:
        print ("Os dois algarismo são IGUAIS")
        igualdade = True

    if soma_compar == key:
        print ("Nennhum algorismo sequencial igual foi encontrado")
        passagem = False
    

