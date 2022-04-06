#receber do usuário, que vai digitar uma sequência de números
#cada número que ele digite eu quero que você imprima o fatorial desse número

key_passage = True
cont = 1
fatorial = 1

while key_passage == True:
    entrada = int(input("Digite um número inteiro positivo que deseja saber o Fatorial: "))
    while entrada < 0 :
        print("Dados de entrada inválido, por gentileza, digite um número inteiro positivo para cálcular o Fatorial: ", end = " ")
        entrada = int(input ())
    key_passage = False
    while cont <= entrada:
        fatorial = fatorial * cont
        cont +=1
    print("Fatorial:",fatorial)
    fatorial = 1
    cont = 1
    if key_passage == False:
        continuar = input ("Voce deseja continuar? (Sim / Não)")
        while continuar != "sim" and continuar != "Não":
            print("Dados de entrada inválido, por gentileza, digite Sim se quiser continuar ou Não se deseja encerrar o programa")
            continuar = input ()
        if continuar == "sim":
                key_passage= True
        else:
            print("programa encerrado")

    
            
            

