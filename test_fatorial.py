def fatorial (n):
    if n <0:
        return 0
    cont = 1
    fatorial = 1
    while cont <= n:
        fatorial = cont * fatorial
        cont = cont+1
    return fatorial

def test_fatorial0():
    assert fatorial(0) == 1

def teste_fatorial1():
    assert fatorial(1) == 1

def teste_fatorial_negativo():
    assert fatorial(-10) == 0

def teste_fatorial4():
    assert fatorial(4)==24

def teste_fatorial5():
    assert fatorial(5)==120

    
