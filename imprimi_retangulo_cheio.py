largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

constroi_larg =2 
constroi_h=0
             
while altura > constroi_h:
    while largura >= constroi_larg:
        print("#",end="")
        constroi_larg+=1
    print("#")
    constroi_h +=1
    constroi_larg = 2
    
