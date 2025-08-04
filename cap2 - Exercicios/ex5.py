# Exercício 5

while True:
    numero = int(input("Digite um número entre 1000 e 9999:"))

    if numero >= 1000 and numero <= 9999:
        break
    else:
        print("Número fora do intervalo pré-definido! Escolha outro número!")

print(f"Unidade: {str(numero)[3]}")
print(f"Dezena: {str(numero)[2]}")
print(f"Centena: {str(numero)[1]}")
print(f"Milhar: {str(numero)[0]}")

