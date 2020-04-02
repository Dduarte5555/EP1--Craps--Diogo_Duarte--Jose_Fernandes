'''Regra Twelve'''
# Regra Twelve consiste em que a aposta possa ser feita em qualquer fase do jogo.
# Nesta aposta se a soma dos dados derem 12 o jogador ganha trinta vezes o que apostou, senão perde a aposta.
if soma == 12:
    fichas == fichas+(aposta*3)
else:
   fichas == fichas - aposta
print(fichas)