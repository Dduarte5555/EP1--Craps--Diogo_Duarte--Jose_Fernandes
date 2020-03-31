#conceitos básicos do game, e introduzir o player
import random 
montante = 1000

#resultados dos dados
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dados = dado1+dado2
print(dados)

#perguntas
pergunta_opção =  input("Qual opção deseja apostar?:  ")
pergunta_aposta = input("Quantas fichas deseja apostar?:  ")
