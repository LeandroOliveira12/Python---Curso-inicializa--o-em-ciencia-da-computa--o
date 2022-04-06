cont = 0
primalidade_1 = 1
primalidade_2 = 1
primalidade_3 = 1

num = int(input("Digite um numero inteiro:"))

primalidade_1 = num %2
primalidade_2 = num %3
primalidade_3 = num %7
primalidade_4 = num %13
primalidade_5 = num%5

if num == 2 or num == 5 or num ==7 or num == 13:
    print ("Primo")
else:
    if num <= 1 or primalidade_1 ==0 or primalidade_2 == 0 or primalidade_3 == 0 or primalidade_4 ==0 or primalidade_5 == 0:
        print ("não Primo")
    else:
        print ("Primo")

    
    


