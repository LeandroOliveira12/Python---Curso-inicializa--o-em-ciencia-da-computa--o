num_entrada = int(input("Insira o numero para saber se ele é FizzBuzz "))

Calc_fizz = num_entrada%5
Calc_buzz = num_entrada%3

if Calc_fizz == 0 and Calc_buzz == 0:
    print ("FizzBuzz")
else:
    print (num_entrada)
