#Dicas DESAFIO FINAL

#- CALMA E PERSISTENCIA
#- DETECTO DE PLÁGIO
#- LER O ENUNCIADO INTEIRO ATÉ O FIM
#- LER UMA SEGUNDA VEZ E PENSAR EM SOLUCIONAR
#- LACUNAS SÃO TRES FUNÇÕES QUE PRECISAMOS IMPLEMENTAR
#- CODIGO DE DETECTÇÃO DE FRASE E SENTENÇA JA ESTÃO PRONTOS
#- BIBLIOTECA RE - EXPRESSOES REGULARES

#Traços linguísticos
#Neste exercício utilizaremos as seguintes estatísticas para detectar a doença:
#Tamanho médio de palavra: Média simples do número de caracteres por palavra.
#Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
#Razão Hapax Legomana: Número de palavras utilizadas uma única vez dividido pelo número total de palavras.
#Tamanho médio de sentença: Média simples do número de caracteres por sentença.
#Complexidade de sentença: Média simples do número de frases por sentença.
#Tamanho médio de frase: Média simples do número de caracteres por frase.


import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os
    textos fornecidos'''
    
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    #As Sentenças são separadas por ponto final, a cada ponto final, ou ! ou ? é inserido um novo item na lista sentencas
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    # Dentro das SENTENÇAS as frases são separadas por , ou : ou ;, inserindo um novo item na lista de frases
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    # Dentro das FRASES as palavras são separadas por ESPAÇOS, inserindo um novo item na lista de palavras
    return frase.split()

def separa_todas_palavras(texto):
  #A funcao recebe um texto e devolve uma lista de todas as palavras dentro dele#
  sentencas = separa_sentencas(texto)
  lista_de_frases = []
  for indice in sentencas:
    frases = separa_frases(indice)
    lista_de_frases.extend(frases)
  lista_de_palavras = []
  for indice in lista_de_frases:
    frases = separa_palavras(indice)
    lista_de_palavras.extend(frases)
  return lista_de_palavras

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    #retorna um numero inteiro com a quantidade de palavras unicas na FRASE
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    #Retorna um numero inteiro com as palavras diferentes dentro da FRASE
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def tamanho_medio_palavra(texto):
  #IMPLEMENTAR. Essa funcao recebe um texto e deve devolver o tamanho medio de suas palavras#
  palavras_separadas = separa_todas_palavras(texto)
  lista_palavras_separadas = []
  for indice in palavras_separadas:
    lista_palavras_separadas.append(len(indice))
  pos_indice = 0
  soma_palavras = 0
  while pos_indice < len(lista_palavras_separadas):
    soma_palavras = soma_palavras + lista_palavras_separadas[pos_indice]
    pos_indice += 1
  return soma_palavras/len(palavras_separadas)

def type_token(texto):
  lista_palavras = separa_todas_palavras(texto)
  return n_palavras_diferentes(lista_palavras)/len(lista_palavras)

def hapax_legomana(texto):
  lista_palavras = separa_todas_palavras(texto)
  return n_palavras_unicas(lista_palavras)/len(lista_palavras)

def tamanho_medio_sentenca(texto):
  qtde_sentencas = len(separa_sentencas(texto))
  comprimento_sentencas = 0
  for indice in separa_sentencas(texto):
    comprimento_sentencas = comprimento_sentencas + len(indice)
  return comprimento_sentencas/qtde_sentencas

def complexidade_sentenca(texto):
  lista_sentencas = separa_sentencas(texto)
  lista_de_frases = []
  for i in lista_sentencas:
    lista_de_frases.extend(separa_frases(i))
  return len(lista_de_frases)/len(lista_sentencas)

def tamanho_medio_frase(texto):
  lista_sentencas = separa_sentencas(texto)
  lista_de_frases = []
  for indice in lista_sentencas:
    lista_de_frases.extend(separa_frases(indice))
  qtde_frases = len(lista_de_frases)
  comprimento_frases = 0
  for frase in lista_de_frases:
    comprimento_frases = comprimento_frases + len(frase)
  return comprimento_frases/qtde_frases


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e'''
    '''deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    valor_minimo = 900
    indice_minimo = -1
    for indice in range(len(textos)):
        valor = compara_assinatura(calcula_assinatura(textos[indice]), ass_cp)
        if valor < valor_minimo:
            valor_minimo = valor
            indice_minimo = indice
    return indice_minimo + 1
  
    assinaturas = [calcula_assinatura(texto) for texto in textos]
    valores = [compara_assinatura(assinatura, ass_cp) for assinatura in assinaturas]
  
    return valores.index(min(valores)) + 1


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    
    tam_medio = tamanho_medio_palavra(texto)
    typ_token = type_token(texto)
    hap_lego = hapax_legomana(texto)
    tam_med_sentenca = tamanho_medio_sentenca(texto)
    comp_sentenca = complexidade_sentenca(texto)
    tam_med_frase = tamanho_medio_frase(texto)
    assinatura = [tam_medio, typ_token, hap_lego, tam_med_sentenca, comp_sentenca, tam_med_frase]
    return assinatura



def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    #IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.#
    #função ABS retorna o módulo cálculado, retirando sinal de nagativo
    somatorio = 0
    for indice in range(len(as_a)):
        valor = abs(as_a[indice] - as_b[indice])
        somatorio += valor
    similaridade = somatorio/6
    return similaridade


#assinatura = le_assinatura()
#textos = le_textos()



