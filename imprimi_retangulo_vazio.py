largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

constroi_larg =1
constroi_h=1


#amz_altura = altura -1

while constroi_h <= altura:
################# linha inicio ###########
    while  constroi_h ==1 and largura >= constroi_larg:
        print("#",end="")
        constroi_larg+=1
    print("")
    constroi_h +=1
    constroi_larg = 1
    
################## linhas do meio ##########
    while constroi_h > 1 and constroi_h < altura:
        if constroi_larg == 1:
            print("#",end="")
            constroi_larg+=1            
        if constroi_larg >= 2 and constroi_larg < largura:
            print(" ",end="")
            constroi_larg+=1
        if constroi_larg >= largura:
            print("#",end="")
            constroi_larg = 1
            constroi_h +=1
            print("")

################## linha final #########
    while  constroi_h == altura and largura >= constroi_larg:
        print("#",end="")
        constroi_larg+=1
    print("")
    constroi_h +=1
    constroi_larg = 1




                
        
    

            
 
        
        
        
        
        
        
        

