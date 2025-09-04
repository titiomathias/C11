import numpy as np

campo = np.array([[0, 0], [0, 0]])

campo[np.random.randint(0, 2)][np.random.randint(0, 2)] = 1

locais = 0

while True:
    if locais == 3:
        print("CONGRATULATIONS! YOU BEAT THE GAME! :)")
        break

    print(campo)

    coluna = int(input("Digite a coluna: "))
    linha = int(input("Digite a linha: "))

    if campo[coluna][linha] == 1:
        print("Pisou na bomba! Perdeu!")
        break
    elif campo[coluna][linha] == -1:
        print("Você já escolheu essa coodernada anteriormente! Tente outra!")
    else:
        locais += 1
        campo[coluna][linha] = -1
        print("Sem bombas por aqui!")