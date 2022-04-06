import math

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

delta = b**2-4*a*c
if delta < 0:
    print ("esta equação não possui raízes reais")
else:
    raiz_delta = math.sqrt(delta)
    x_pos = (-(b)+raiz_delta)/(2*a)
    x_neg = (-(b)-raiz_delta)/(2*a)
        
    if delta == 0:
        print("a raiz desta equação é",x_pos)

    if delta > 0:
        if x_pos < x_neg:
            print("as raízes da equação são",x_pos,"e", x_neg)
        else:
            print("as raízes da equação são",x_neg,"e", x_pos)
