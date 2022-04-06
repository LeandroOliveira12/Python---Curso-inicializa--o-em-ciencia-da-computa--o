#Programa Leitor de Cartão


MeuCartão = int(input("Digite o primeiro número do seu Cartão de crédito: "))
CartãoLido = 1
encontreiMeuCartãoNaLista = False

while CartãoLido != 0 and not encontreiMeuCartãoNaLista:
    CartãoLido = int(input("Digite o número do próximo Cartão de crédito: "))
    if CartãoLido == MeuCartão:
        encontreiMeuCartãoNaLista = True

if encontreiMeuCartãoNaLista :
    print ("EBA!! Meu Cartão está lá !!")
else:
    print ("Xii !! Meu Cartão não está lá !!")
