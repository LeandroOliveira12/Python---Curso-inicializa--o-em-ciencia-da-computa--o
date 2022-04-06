n = int(input("Digite a ordem N, para calculo do coeficiente binomial"))
k = int(input("Digite a classe K, para calculo do coeficiente binomial"))


def fatorial (fat):
    cont =1
    fatorial=1
    while cont <= fat:
        fatorial = cont * fatorial
        cont = cont+1
    return fatorial

def numero_binomial(n,k):
    return fatorial(n)/(fatorial(k)*fatorial(n-k))
    

ordem = fatorial(n)
classe = fatorial(k)
sub = fatorial(n-k)

print("o coeficiente binomial é:",int(ordem/(classe*sub)))














