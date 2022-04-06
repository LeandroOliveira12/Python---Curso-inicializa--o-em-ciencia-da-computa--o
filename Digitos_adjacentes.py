
num = int(input("Digite o numero: "))


igualdade = False
atual = 0
anterior = 1
soma_compar = 0


entrada = num
key = 0
cont = 0
soma = 0
passagem = True

if num != 0:
    while cont < 100:
        soma = entrada % 10
        entrada = entrada // 10
        key = key + soma
        cont  = cont + 1

    while igualdade == False and passagem == True: 
        anterior = num % 10
        num = num // 10
        soma_compar = anterior + soma_compar    
        atual = num % 10

        if anterior == atual:
            print ("sim")
            igualdade = True

        if soma_compar == key and anterior != atual:
           print ("não")
           passagem = False
else:
    print ("não")
    

