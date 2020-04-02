'''Regra Any Craps'''
#Esta aposta pode ser feita em qualquer momento do jogo
#Se os dados derem 2, 3 ou 12 o jogador ganha 7 vezes o valor apostado
if dados == 2  or 3 or 12:
    montante = montante + aposta*7
else:
    montate = montante - aposta
print (montante)

