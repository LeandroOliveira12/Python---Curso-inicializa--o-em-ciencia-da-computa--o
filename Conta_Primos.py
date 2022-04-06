#Escreva a função n_primos que recebe como argumento um número inteiro maior ou igual a 2 como parâmetro
#e devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).

#informa o maior numero primo possivel
def n_primos (num):
    cont = 1
    primo = 0
    qtd_primo = 0
    while (cont <= num):
    
        primalidade_1 = cont %2
        primalidade_2 = cont %3
        primalidade_3 = cont %7
        primalidade_4 = cont %13
        primalidade_5 = cont%5

        if cont == 2 or cont ==3 or cont == 5 or cont ==7 or cont == 13: #Verfica se é Primo
            #print ("Primo2")
            primo=cont
            qtd_primo += 1
        else:
            if cont <= 1 or primalidade_1 ==0 or primalidade_2 == 0 or primalidade_3 == 0 or primalidade_4 ==0 or primalidade_5 == 0: #verifica se é Primo
                primo=primo
            else:
                primo=cont
                qtd_primo += 1
               # print ("qtd", qtd_primo)
        cont = cont + 1
    return qtd_primo
                
