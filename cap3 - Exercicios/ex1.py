# Colocados de um Campeonato de Xadrez (não manjo de futebol kkkk)
colocados = ["Magnus Carlsen", "Hikaru Nakamura", "Fabiano Caruana", "Praggnanandhaa Rameshbabu", "Gukesh Dommaraju"]

# 1.a
print("Top 3: ", colocados[0:3])

# 1.b
print("2 últimos: ", colocados[3:])

# 1.c
print("Colocados ordenados:")
for nome in sorted(colocados): print(nome)

# 1.d (Em que posição da tabela se encontra Hikaru Nakamura, melhor jogador de Blitz!)
print("Posição de Hikaru: ", colocados.index("Hikaru Nakamura")+1) # Somo um para que seja condizente com o rank mundial (não existe posição 0 no rank)

