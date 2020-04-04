#conceitos básicos do game, e introduzir o player
import random 
fichas = 1000


'''Regra Pass Line Bet'''
#Essa aposta só pode ser feita na primeira fase (Come Out)
#Se a soma dos dados for 7 ou 11 o jogador ganha o dobro de sua aposta
#Se a soma dos dados for 2, 3 ou 12 (Craps) o jogador perde sua aposta
#Se a soma dos dados for 4,5,6,8,9 ou 10 o jogo vai para a fase Point e a aposta continua
#Na fase point o objetivo do jogador é que saia o mesmo valor da fase Come Out
#Se esse valor sair ele ganha o dobro do apostado, se sair a soma 7 ele perde tudo
#Caso saia qualquer outro valor o jogo continua em Point até sair 7 ou o objetivo do jogador

def pass_line_bet1(soma, fichas, aposta1):
    if soma in [7, 11]:
        fichas = fichas + aposta1
    if soma in [2, 3, 12]:
        fichas = fichas - aposta1
    return (fichas)


def pass_line_bet2(fichas, aposta1):
    contador = True
    while contador:
        dado3 = random.randint(1, 6)
        dado4 = random.randint(1, 6)
        soma_plb_point = dado3 + dado4
        print(soma_plb_point)
        if soma_plb_point in [7]:
            fichas = fichas - aposta1
            contador = False
        elif soma_plb_point in [soma]:
            fichas = fichas + aposta1
            contador = False
        else:
            continue
    return (fichas)

'''Regra Field'''
#Pode ser feita em qualquer parte do jogo
#Se a soma dos dados derem 5, 6, 7 ou 8, perde a toda a aposta
#Se a soma der 3, 4, 9, 10 ou 11, ganha o mesmo valor da aposta
#Se a soma der 2, ganha o valor da aposta 2 vezes
#Se a soma der 12, ganha o valor da aposta 3 vezes
def field(soma, fichas, aposta2):
    if soma in [5, 6, 7, 8]:
        fichas2 = fichas - aposta2
    if soma in [3, 4, 9, 10, 11]:
        fichas2 = fichas + aposta2
    if soma == 2:
        fichas2 = fichas + (aposta2)*2
    if soma == 12:
        fichas2 = fichas + (aposta2)*3
    else:
        pass
    return (fichas2)


'''Regra Any Craps'''
#Esta aposta pode ser feita em qualquer momento do jogo
#Se a soma dos dados derem 2, 3 ou 12 o jogador ganha 7 vezes o valor apostado
def any_craps(soma, fichas, aposta3):
    if soma in [2, 3, 12]:
        fichas = fichas + (aposta3)*7
    elif soma in [1, 4, 5, 6, 7, 8, 9, 10, 11]:
        fichas = fichas-aposta3
    else: 
        pass
    return (fichas)


'''Regra Twelve'''
#Regra Twelve consiste em que a aposta possa ser feita em qualquer fase do jogo.
#Nesta aposta se a soma dos dados derem 12 o jogador ganha trinta vezes o que apostou, senão perde a aposta.
def twelve(soma, fichas, aposta4):
    if soma == 12:
        fichas = fichas+((aposta4)*30)
    else:
        fichas = fichas - aposta4
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
        if apostar_ou_sair == 'apostar':
            print('VOCÊ ESTÁ EM COME OUT')
            print(fichas)
            #resultados dos dados
            dado1 = random.randint(1, 6)
            dado2 = random.randint(1, 6)
            soma = dado1+dado2
            modo_de_aposta2 =  input('Você deseja apostar em Field? (sim/não)  ')
            if modo_de_aposta2=='sim':
                aposta2 = int(input('Quantas fichas deseja apostar?:  '))
                fichas = field(soma, fichas, aposta2)
            elif modo_de_aposta2=='não': 
                pass
            else: 
                pass
            print(fichas)
            modo_de_aposta3 =  input('Você deseja apostar em Any Craps? (sim/não)  ')
            if modo_de_aposta3=='sim':
                aposta3 = int(input('Quantas fichas deseja apostar?:  '))
                fichas = any_craps(soma, fichas, aposta3)
            elif modo_de_aposta3=='não': 
                pass
            else: 
                pass
            print(fichas)
            modo_de_aposta4 =  input('Você deseja apostar em Twelve? (sim/não)  ')
            if modo_de_aposta4=='sim':
                aposta4 = int(input('Quantas fichas deseja apostar?:  '))
                fichas = twelve(soma, fichas, aposta4)
            elif modo_de_aposta4=='não': 
                pass
            else: 
                pass             
            print(fichas)
            modo_de_aposta1 =  input('Você deseja apostar em Pass Line Bat? (sim/não)  ')
            if modo_de_aposta1=='sim':
                aposta1 = int(input('Quantas fichas deseja apostar?:  '))
                fichas = pass_line_bet1(soma, fichas, aposta1)
                if soma in [4, 5, 6, 8, 9, 10]: 
                    print('VOCÊ ESTÁ EM POINT')
                    print(fichas)
                    fichas = pass_line_bet2(fichas, aposta1)
                    dado5 = random.randint(1, 6)
                    dado6 = random.randint(1, 6)
                    nova_soma = dado5 + dado6
                    print(fichas)
                    modo_de_aposta2 =  input('Você deseja apostar em Field? (sim/não)  ')
                    if modo_de_aposta2=='sim':
                        aposta2 = int(input('Quantas fichas deseja apostar?:  '))
                        fichas = field(nova_soma, fichas, aposta2)
                    elif modo_de_aposta2=='não': 
                        pass
                    else: 
                        pass
                    print(fichas)
                    modo_de_aposta3 =  input('Você deseja apostar em Any Craps? (sim/não)  ')
                    if modo_de_aposta3=='sim':
                        aposta3 = int(input('Quantas fichas deseja apostar?:  '))
                        fichas = any_craps(nova_soma, fichas, aposta3)
                    elif modo_de_aposta3=='não': 
                        pass
                    else:
                        pass
                    print(fichas)
                    modo_de_aposta4 =  input('Você deseja apostar em Twelve? (sim/não)  ')
                    if modo_de_aposta4=='sim':
                        aposta4 = int(input('Quantas fichas deseja apostar?:  '))
                        fichas = twelve(nova_soma, fichas, aposta4)
                    elif modo_de_aposta4=='não': 
                        pass     
                    else:
                        pass
                    print(fichas)                           
            elif modo_de_aposta1=='não': 
                pass
            else:
                pass
print('Você terminou o jogo com {} fichas.'.format(fichas))
