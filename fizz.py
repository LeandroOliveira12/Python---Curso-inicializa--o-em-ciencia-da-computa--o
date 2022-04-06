num_entrada = int(input("Insira o numero para saber se ele é Buzz "))

Calc_num = num_entrada%5

if Calc_num == 0:
    print ("Buzz")
else:
    print (num_entrada)
