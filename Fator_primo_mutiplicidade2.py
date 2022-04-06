#Dado número inteiro n, sendo que n é maior que 1,
#positivo maior que 1 imprimir a sua decomposição fatores primos indicando também a multiplicidade de cada fator.
import math
    
def Fator_primo ():

    print("Programa que decompoe os Fatores Primos, e indica da multiplicidade de cada fator")
    entrada = int(input("Digite um número inteiro positivo: "))

    fator = 2
    multiplicidade = 0
    valida_entrada =1

    while entrada > 1:
        while entrada % fator ==0:
            multiplicidade += 1
            entrada = entrada/ fator
        if multiplicidade > 0:
            print ("Fator ", fator, "Multiplicidade = ", multiplicidade)
        valida_entrada = valida_entrada * math.pow(fator,multiplicidade)
        fator = fator + 1
        multiplicidade = 0
    print("Valida entrada:", valida_entrada)


Fator_primo()


