import numpy as np

# 1.a

arr1 = np.ones(8)
arr2 = np.random.randint(0, 10, size=8)
arr3 = arr1 + arr2

print(arr3)

if arr3.sum() >= 40:
    mtz = arr3.reshape(2, 4)
else:
    mtz = arr3.reshape(4, 2)

print(mtz)


# 2
parr1 = np.arange(0, 51, 2)
parr2 = np.arange(50, 101, 2)
parr3 = np.concatenate((parr1, parr2))

print(parr1)
print(parr2)
print(parr3)


# 3
mtz2 = np.zeros(4)
mtz2[np.random.randint(0, 4)] = 1
mtz2 = mtz2.reshape(2, 2)

while True:
    linha = int(input("Digite o número da linha (0 ou 1): "))
    coluna = int(input("Digite o número da coluna (0 ou 1): "))

    if mtz2[linha, coluna] == 1:
        print("Boom! Você acertou a bomba!")
        break
    elif mtz2[linha, coluna] == -1:
        print("Você já escolheu esse lugar. Tente outro!")
    else:
        mtz2[linha, coluna] = -1
        if mtz2.sum() == -2:
            print("Parabéns! Você encontrou todos os lugares seguros!")
            break
        else:
            print("Lugar seguro. Continue procurando!")
    

# 4
mtz = np.zeros((np.random.randint(0, 10), np.random.randint(0, 10)))
l, c = mtz.shape
if l*c % 2 == 0:
    print("A matriz tem um número par de elementos.")
else:
    print("A matriz tem um número ímpar de elementos.")


# 5
np.random.seed(10)
mtz4 = np.random.randint(1, 51, size=(4, 4))
medias_linhas = np.array([])
medias_colunas = np.array([])

for i in range(4):
    print("Média da linha", i+1, ":", mtz4[i].mean())
    medias_linhas = np.append(medias_linhas, mtz4[i].mean())
    print("Média da coluna", i+1, ":", mtz4[:, i].mean())
    medias_colunas = np.append(medias_colunas, mtz4[:, i].mean())

print("Maior média entre as linhas:", medias_linhas.max())
print("Maior média entre as colunas:", medias_colunas.max())

numeros = np.unique(mtz4, return_counts=True)
print("Números que se repetem e suas quantidades:")
for num, count in zip(numeros[0], numeros[1]):
    print(f"Número {num} aparece {count} vezes")

for num, count in zip(numeros[0], numeros[1]):
    if count == 2:
        print(f"Número {num} aparece exatamente duas vezes")


