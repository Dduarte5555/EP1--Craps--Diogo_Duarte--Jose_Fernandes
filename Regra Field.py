""" Regra Field"""
#Pode ser feita em qualquer parte do jogo
#Se a soma dos dados derem 5, 6, 7 ou 8, perde a toda a aposta
#Se a soma der 3, 4, 9, 10 ou 11, ganha o mesmo valor da aposta
#Se a soma der 2, ganha o valor da aposta 2 vezes
#Se a soma der 12, ganha o valor da aposta 3 vezes

if soma == 5 or 6 or 7 or 8:
    ficha = ficha
elif soma == 3 or 4 or 9 or 10 or 11:
    ficha = ficha + (aposta*2)
elif soma == 2:
    ficha = ficha + (aposta*3)
elif soma == 12:
    ficha = ficha + (aposta*4)