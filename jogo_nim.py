total_peças_n = 0
limites_jogadas_m = 0
vitoria_usuario = 0
vitoria_computador=0



def computador_escolhe_jogada(n,m):
    m_mais_um = m +1

    if m == 1:
        retira_pecas_PC = m
        return retira_pecas_PC
    
    if n <= m:
        retira_pecas_PC = n
        return retira_pecas_PC
    else:
        resto = n%m_mais_um

        if resto > 0:
            retira_pecas_PC = resto
            return retira_pecas_PC
        
        return m

        
def usuario_escolhe_jogada(n,m):
    retira_pecas_usuário=0
    
    retira_pecas_usuário = int(input("Quantas peças você vai tirar?"))
                           
    while retira_pecas_usuário > m or retira_pecas_usuário <= 0:
        print("Oops! Jogada inválida! Tente de novo.")
        retira_pecas_usuário = int(input("Quantas peças você vai tirar?"))
                        
    return retira_pecas_usuário


def teste_multiplo_m(n_test,m_test):
    mult = m_test+1
    checa_multiplo = n_test% mult

    if checa_multiplo == 0:
        multiplo = True
    else:
        multiplo = False
    return multiplo    

def partida ():
    global vitoria_computador
    global vitoria_usuario
    
    total_peças_n = int(input("Quantas peças?"))
    limites_jogadas_m = int(input("Limite de peças por jogada?"))

    multiplo = teste_multiplo_m(total_peças_n,limites_jogadas_m)

    if multiplo == True:
        print("Voce começa!")
        while total_peças_n !=0:
            pecas_removidas_usuario = usuario_escolhe_jogada(total_peças_n,limites_jogadas_m)
            
                    #QUANTAS PEÇAS FORAM REMOVIDAS NA ÚLTIMA JOGADA USUÁRIO
            if pecas_removidas_usuario == 1:
                total_peças_n = total_peças_n - pecas_removidas_usuario
                print("você tirou uma peça.")
                
            if pecas_removidas_usuario > 1:
                total_peças_n = total_peças_n - pecas_removidas_usuario
                print("você tirou",pecas_removidas_usuario,"peças.")
                
                    #QUANTAS RESTAM NA MESA
            if total_peças_n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            if total_peças_n >1 :
                print("Agora restam",total_peças_n,"peças no tabuleiro.")
            if total_peças_n == 0:
                print("Fim do jogo! Você ganhou!")
                vitoria_usuario = vitoria_usuario+1
                return 

   
            peças_removidas_PC = computador_escolhe_jogada(total_peças_n, limites_jogadas_m)
            
                #QUANTAS PEÇAS FORAM REMOVIDAS NA ÚLTIMA JOGADA PC
            if peças_removidas_PC == 1:
                total_peças_n = total_peças_n - peças_removidas_PC
                print("O Computador tirou uma peça.")
                
            if peças_removidas_PC > 1:
                total_peças_n = total_peças_n - peças_removidas_PC
                print("O computador tirou",peças_removidas_PC,"peças.")
                
                    #QUANTAS RESTAM NA MESA
            if total_peças_n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            if total_peças_n >1 :
                print("Agora restam",total_peças_n,"peças no tabuleiro.")
            if total_peças_n == 0:
                print("Fim do jogo! O computador ganhou!")
                vitoria_computador = vitoria_computador+1
                return 



            
    if multiplo == False:
        print("Computador começa!")
        while total_peças_n !=0:
            peças_removidas_PC = computador_escolhe_jogada(total_peças_n, limites_jogadas_m)
            
                #QUANTAS PEÇAS FORAM REMOVIDAS NA ÚLTIMA JOGADA PC
            if peças_removidas_PC == 1:
                total_peças_n = total_peças_n - peças_removidas_PC
                print("O Computador tirou uma peça.")
                
            if peças_removidas_PC > 1:
                total_peças_n = total_peças_n - peças_removidas_PC
                print("O computador tirou",peças_removidas_PC,"peças.")
                
                    #QUANTAS RESTAM NA MESA
            if total_peças_n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            if total_peças_n >1 :
                print("Agora restam",total_peças_n,"peças no tabuleiro.")
            if total_peças_n == 0:
                print("Fim do jogo! O computador ganhou!")
                vitoria_computador = vitoria_computador+1
                return 
            
            pecas_removidas_usuario = usuario_escolhe_jogada(total_peças_n,limites_jogadas_m)
            
                    #QUANTAS PEÇAS FORAM REMOVIDAS NA ÚLTIMA JOGADA USUÁRIO
            if pecas_removidas_usuario == 1:
                total_peças_n = total_peças_n - pecas_removidas_usuario
                print("você tirou uma peça.")
                
            if pecas_removidas_usuario >1:
                total_peças_n = total_peças_n - pecas_removidas_usuario
                print("você tirou",pecas_removidas_usuario,"peças.")
                
                    #QUANTAS RESTAM NA MESA
            if total_peças_n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            if total_peças_n >1 :
                print("Agora restam",total_peças_n,"peças no tabuleiro.")
            if total_peças_n == 0:
                print("Fim do jogo! Você ganhou!")
                vitoria_usuario = vitoria_usuario+1
                return 

def campeonato ():
    #chamar a função partida 3 vezes
    cont = 1
    while cont <= 3:
        print("**** Rodada ",cont," ****")
        partida()
        cont = cont +1
    print("**** Final do campeonato! ****\n")    
    print("Placar: Você", vitoria_usuario," X ",vitoria_computador," Computador")
        



def main():
    print ("Bem-vindo ao jogo  no NIM! Escolha: ")

    tipo_jogo = int(input(" 1 - para jogar uma partida isolada \n 2 - para jogar um campeonato\n"))

    if tipo_jogo == 1:
        print ("Voce escolheu uma Partida!")
        partida()

    if tipo_jogo == 2:
        print ("Voce escolheu um campeonato!")
        campeonato ()




main()


    


    

    
    
    
    
