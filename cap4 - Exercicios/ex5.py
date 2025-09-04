import numpy as np

np.random.seed(10)

matriz = np.array(np.random.randint(1, 50, [4,4]))

print(matriz)

print("Média de cada linha e cada coluna: ")

linhas = []
colunas = []

for i in range(0, matriz.shape[0]):
    mediaL = sum(matriz[i, :])/matriz.shape[0]
    print(f"Média da linha {i} = ", mediaL)
    linhas.append(mediaL)


for i in range(0, matriz.shape[1]):
    mediaC = sum(matriz[:, i])/matriz.shape[1]
    print("Média da coluna {i}", mediaC)
    colunas.append(mediaC)


print("Maior média de linhas: ", np.array(linhas).max())
print("Maior média de colunas: ", np.array(colunas).max())

