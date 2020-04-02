#conceitos básicos do game, e introduzir o player
import random 
fichas = 1000

#resultados dos dados
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
soma = dado1+dado2


dado5 = random.randint(1, 6)
dado6 = random.randint(1, 6)
nova_soma = dado5 + dado6

#perguntas
#pergunta_opção =  input('Qual opção deseja apostar?:  ')
#aposta = int(input('Quantas fichas deseja apostar?:  '))

'''Regra Pass Line Bet'''
#Essa aposta só pode ser feita na primeira fase (Come Out)
#Se a soma dos dados for 7 ou 11 o jogador ganha o dobro de sua aposta
#Se a soma dos dados for 2, 3 ou 12 (Craps) o jogador perde sua aposta
#Se a soma dos dados for 4,5,6,8,9 ou 10 o jogo vai para a fase Point e a aposta continua
#Na fase point o objetivo do jogador é que saia o mesmo valor da fase Come Out
#Se esse valor sair ele ganha o dobro do apostado, se sair a soma 7 ele perde tudo
#Caso saia qualquer outro valor o jogo continua em Point até sair 7 ou o objetivo do jogador

lista_point = [4, 5, 6, 8, 9, 10]
def pass_line_bet1(soma, fichas, aposta1):
    if soma == 7 or 11:
        fichas = fichas+((aposta1)*2)
    elif soma == 2 or 3 or 12:
        fichas = fichas
    elif soma == 4 or 5 or 6 or 8 or 9 or 10: 
        print('VOCÊ ESTÁ EM POINT')
    return (fichas)

def pass_line_bet2(fichas, aposta1):
    contador = True
    while contador:
        dado3 = random.randint(1, 6)
        dado4 = random.randint(1, 6)
        soma_plb_point = dado3 + dado4
        if soma_plb_point == 7:
            fichas = fichas
        elif soma_plb_point == soma:
            fichas = fichas + ((aposta1)*2)
        else:
            continue


'''Regra Field'''
#Pode ser feita em qualquer parte do jogo
#Se a soma dos dados derem 5, 6, 7 ou 8, perde a toda a aposta
#Se a soma der 3, 4, 9, 10 ou 11, ganha o mesmo valor da aposta
#Se a soma der 2, ganha o valor da aposta 2 vezes
#Se a soma der 12, ganha o valor da aposta 3 vezes
def field(soma, fichas, aposta2):
    if soma == 5 or 6 or 7 or 8:
        fichas = fichas
    elif soma == 3 or 4 or 9 or 10 or 11:
        fichas = fichas + ((aposta2)*2)
    elif soma == 2:
        fichas = fichas + ((aposta2)*3)
    elif soma == 12:
        fichas = fichas + ((aposta2)*4)
    return(fichas)

'''Regra Any Craps'''
#Esta aposta pode ser feita em qualquer momento do jogo
#Se a soma dos dados derem 2, 3 ou 12 o jogador ganha 7 vezes o valor apostado
def any_craps(soma, fichas, aposta3):
    if soma == 2  or 3 or 12:
        fichas = fichas + (aposta3)*7
    else:
        fichas = fichas - aposta3
    return (fichas)

'''Regra Twelve'''
#Regra Twelve consiste em que a aposta possa ser feita em qualquer fase do jogo.
#Nesta aposta se a soma dos dados derem 12 o jogador ganha trinta vezes o que apostou, senão perde a aposta.
def twelve(soma, fichas, aposta4):
    if soma == 12:
        fichas == fichas+((aposta4)*3)
    else:
        fichas == fichas - aposta4
    return (fichas)

jogo = True
while jogo:
    if fichas<=0:
        jogo = False
    else:
        print(fichas) 
        apostar_ou_sair = input('Você deseja apostar ou sair? (apostar/sair)')
        if apostar_ou_sair=='sair':
            jogo = False
        elif apostar_ou_sair == 'apostar':
            print('VOCÊ ESTÁ EM COME OUT')
            print(fichas)
            modo_de_aposta2 =  input('Você deseja apostar em Field? (sim/não)  ')
            if modo_de_aposta2=='sim':
                aposta2 = int(input('Quantas fichas deseja apostar?:  '))
                fichas = fichas - aposta2
                field(soma, fichas, aposta2)
                print(fichas)
            elif modo_de_aposta2=='não': 
                pass
            modo_de_aposta3 =  input('Você deseja apostar em Any Craps? (sim/não)  ')
            if modo_de_aposta3=='sim':
                    aposta3 = int(input('Quantas fichas deseja apostar?:  '))
                    fichas = fichas - aposta3
                    any_craps(soma, fichas, aposta3)
                    print(fichas)
            elif modo_de_aposta3=='não': 
                pass
            modo_de_aposta4 =  input('Você deseja apostar em Twelve? (sim/não)  ')
            if modo_de_aposta4=='sim':
                    aposta4 = int(input('Quantas fichas deseja apostar?:  '))
                    fichas = fichas - aposta4
                    any_craps(soma, fichas, aposta4)
                    print(fichas)
            elif modo_de_aposta4=='não': 
                pass             
            modo_de_aposta1 =  input('Você deseja apostar em Pass Line Bat? (sim/não)  ')
            if modo_de_aposta1=='sim':
                aposta1 = int(input('Quantas fichas deseja apostar?:  '))
                fichas = fichas - aposta1
                pass_line_bet1(soma, fichas, aposta1)
                print(fichas)
                if soma in lista_point:
                    print(fichas)
                    pass_line_bet2(fichas, aposta1)
                    modo_de_aposta2 =  input('Você deseja apostar em Field? (sim/não)  ')
                    if modo_de_aposta2=='sim':
                        aposta2 = int(input('Quantas fichas deseja apostar?:  '))
                        fichas = fichas - aposta2
                        field(nova_soma, fichas, aposta2)
                        print(fichas)
                    elif modo_de_aposta2=='não': 
                        pass
                    modo_de_aposta3 =  input('Você deseja apostar em Any Craps? (sim/não)  ')
                    if modo_de_aposta3=='sim':
                        aposta3 = int(input('Quantas fichas deseja apostar?:  '))
                        fichas = fichas - aposta3
                        any_craps(nova_soma, fichas, aposta3)
                        print(fichas)
                    elif modo_de_aposta3=='não': 
                        pass
                    modo_de_aposta4 =  input('Você deseja apostar em Twelve? (sim/não)  ')
                    if modo_de_aposta4=='sim':
                        aposta4 = int(input('Quantas fichas deseja apostar?:  '))
                        fichas = fichas - aposta4
                        any_craps(nova_soma, fichas, aposta4)
                        print(fichas)
                    elif modo_de_aposta4=='não': 
                        pass                                
            elif modo_de_aposta1=='não': 
                pass
            

print('Você terminou o jogo com {} fichas.'.format(fichas))
