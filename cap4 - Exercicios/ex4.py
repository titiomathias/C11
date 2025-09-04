import numpy as np

matriz = np.zeros((np.random.randint(1, 5), np.random.randint(1, 5)))

print(matriz)

linhas, colunas = matriz.shape

n = linhas*colunas

if n%2 == 0:
    print("Pode se tornar um vetor unidimensional com número PAR de elementos.")
else:
    print("Pode se tornar um vetor unidimensional com número ÍMPAR de elementos.")