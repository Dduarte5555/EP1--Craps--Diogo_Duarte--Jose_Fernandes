'''Regra Any Craps'''
#Esta aposta pode ser feita em qualquer momento do jogo
#Se a soma dos dados derem 2, 3 ou 12 o jogador ganha 7 vezes o valor apostado
if soma == 2  or 3 or 12:
    fichas = fichas + aposta*7
else:
    fichas = fichas - aposta
print (fichas)

