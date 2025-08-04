# Exercícios

while True:
    sexo = input("Digite qual o gênero você se identifica -> [M]asculino ou [F]eminino: ").lower()

    if sexo == "m":
        print("Você se identifica com o sexo masculino!")
        break
    elif sexo == "f":
        print("Você se identifica com sexo feminino!")
        break
    else:
        print("Opção inválida! Tente novamente.")
