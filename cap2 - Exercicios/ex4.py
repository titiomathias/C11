# Exercício 4

d = float(input("Digite a distância da viagem em km: "))

if d <= 200.00:
    valor = d*0.5
else:
    valor = d*0.45

print(f"O valor da passagem ficou em: R${valor:.2f}")