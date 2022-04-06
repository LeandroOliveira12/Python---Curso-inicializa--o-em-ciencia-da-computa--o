while (1):
    num_one = int(input("Insira o numero para a 1° posição "))
    num_two = int(input("Insira o numero para a 2° posição "))
    num_three = int(input("Insira o numero para a 3° posição "))

    x = num_one <= num_two
    y = num_two <= num_three
    z = num_one <= num_three

    if x == True and y == True and z == True:
        print ("crescente")
    else:
        print ("não está em ordem crescente")



