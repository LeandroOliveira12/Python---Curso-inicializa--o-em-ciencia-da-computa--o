import math

x_um = int(input("Digite o valor de X1: "))
y_um = int(input("Digite o valor de Y1: "))
x_dois = int(input("Digite o valor de X2: "))
y_dois = int(input("Digite o valor de Y2: "))

dist = math.sqrt(((x_um - x_dois)**2)+((y_um - y_dois)**2))

if dist >= 10:
    print ("longe")
else:
    print ("perto")
