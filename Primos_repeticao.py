def Primalidade(entrada):
    fator =2
    if entrada == 2:
        return True
    while entrada % fator != 0 and fator <= entrada/2:
        fator +=1
    if entrada % fator ==0:
        return False
    else:
        return True

entrada = int(input("Digite um número inteiro: "))

while entrada>0:
    if Primalidade(entrada):
        print ("É Primo!")
    else:
        print ("Não é primo :-(")
        print("cont: ",cont)
    entrada = int(input("Digite um número inteiro: "))
    
        
    
