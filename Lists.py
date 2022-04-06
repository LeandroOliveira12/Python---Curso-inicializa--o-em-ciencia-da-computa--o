#Vou deixar de lição de casa exercício para vocês. Faça programa que vai lendo do teclado
#uma sequência de números inteiros terminadas por zero e quando o usuário digita o zero,
#ele imprimi essa sequência na ordem inversa. Na ordem ao contrário da ordem que o usuário digitou.
#O único jeito de implementar isso é usando uma lista, então, por favor, tentem fazer isso
num_int = []

entrada = int(input("Digite um número inteiro: "))

cont=0

num_int.append(entrada)
while entrada != 0:
    cont +=1
    entrada = int(input("Digite um número inteiro: "))
    num_int.append(entrada)

if entrada == 0:
    while cont != 0:
        print (num_int[(cont-1)])
        cont = cont - 1



    
