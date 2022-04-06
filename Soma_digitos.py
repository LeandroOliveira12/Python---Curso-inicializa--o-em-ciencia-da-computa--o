
num_calc = int(input("Digite o numero que deseja somar os digitos: "))
result = 0
soma = 0
cont = 0
while cont != 15:

    num1 = num_calc % 10
    soma = soma + num1
    num_calc = num_calc // 10
    cont = cont + 1 
print (soma)

