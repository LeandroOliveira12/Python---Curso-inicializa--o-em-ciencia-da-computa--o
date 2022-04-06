linha = 1
coluna = 1

tabu = False
while linha <= 10:
    tabu = True
    while coluna <= 10:
        if tabu == True:
            print ("Tabuada do ", linha,":" ,end = " ")
            tabu = False
        print (linha * coluna, end = "\t")
        coluna = coluna+1
    linha = linha +1
    print()
    coluna = 1
