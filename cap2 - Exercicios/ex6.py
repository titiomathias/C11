# Exercício 6
import math

n = float(input("Digite um número com casas decimais: "))

print(f"Raiz: {math.sqrt(n)}")
print(f"Teto: {math.ceil(n)}")
print(f"Chão: {math.floor(n)}")

print(str(n))

print(f"Sua parte inteira: {str(n).split(".")[0]}")