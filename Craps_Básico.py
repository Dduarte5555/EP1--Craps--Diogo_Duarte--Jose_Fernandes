#conceitos básicos do game, e introduzir o player
import random 
ficha = 1000

#resultados dos dados
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
soma = dado1+dado2
print(soma)

#perguntas
pergunta_opção =  input("Qual opção deseja apostar?:  ")
aposta = int(input("Quantas fichas deseja apostar?:  "))
