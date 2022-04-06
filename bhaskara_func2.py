import math

def delta (a,b,c):
    return b**2-4*a*c

def main():
    a_digitado = int(input("Digite o valor de A: "))
    b_digitado = int(input("Digite o valor de B: "))
    c_digitado = int(input("Digite o valor de C: "))
    imprime_raizes(a_digitado,b_digitado,c_digitado)

def imprime_raizes(a,b,c):
    d = delta(a,b,c)
    if d ==0:
        raiz1 = (-b+ math.sqrt(d))/(2*a)
        print("a unica raiz é:", raiz1)
    else:
            if d <0:
                print("esta equação não possui raizes")
            else:
                raiz1 = (-b + math.sqrt(d))/(2*a)
                raiz2 = (-b - math.sqrt(d))/(2*a)
                print ("a primeira raiz é: ", raiz1)
                print("a segunda raiz é: ", raiz2)



  
