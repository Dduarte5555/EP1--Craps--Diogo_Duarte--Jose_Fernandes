# Regra Twelve consiste em que a aposta possa ser feita em qualquer fase do jogo.
# Nesta aposta se o dados derem 12 o jogador ganha trinta vezes o que apostou, senão perde a aposta.
if resultado == 12:
    montante == montante+(aposta*3)
else:
    montante == montante-aposta
print(montante)