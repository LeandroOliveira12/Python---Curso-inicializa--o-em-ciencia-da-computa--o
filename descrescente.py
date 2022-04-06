#Programa Indicador de passagem
decrescente = True
anterior = int(input("Digite o primeiro número da sequencia: "))
valor = 1

while valor != 0 and decrescente:
    valor = int(input("Digite um número da sequência: "))
    if valor > anterior:
        decrescente = False
    anterior = valor

if decrescente :
    print ("A sequencia está em ordem descrecente! :-) ")
else:
    print ("A sequencia não está em ordem descrecente! :-( ")
