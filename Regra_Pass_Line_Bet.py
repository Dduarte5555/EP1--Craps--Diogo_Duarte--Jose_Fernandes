'''Regra Pass Line Bet'''
#Essa aposta só pode ser feita na primeira fase (Come Out)
#Se a soma dos dados for 7 ou 11 o jogador ganha o dobro de sua aposta
#Se a soma dos dados for 2, 3 ou 12 (Craps) o jogador perde sua aposta
#Se a soma dos dados for 4,5,6,8,9 ou 10 o jogo vai para a fase Point e a aposta continua
#Na fase point o objetivo do jogador é que saia o mesmo valor da fase Come Out
#Se esse valor sair ele ganha o dobro do apostado, se sair a soma 7 ele perde tudo, e caso saia qualquer outro valor o jogo continua em Point até sair 7 ou o objetivo
import random

if soma == 7 or 11:
    ficha = ficha+(aposta*2)
elif soma == 2 or 3 or 12:
    ficha = ficha
elif soma == 4 or 5 or 6 or 8 or 9 or 10: 
    dado3 = random.randint(1,6)
    dado4 = random.randint(1,6)
    novasoma = dado3+dado4
    print('Você está na fase Point')
    if novasoma == soma:
        ficha = ficha+(aposta*2)
    elif novasoma == 7:
        ficha = ficha 
    else: 
        pass
else:
    pass


        


