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
print(mtz.shape)