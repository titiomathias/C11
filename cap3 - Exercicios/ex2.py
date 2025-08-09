# Exercício dos smartphones

loja1 = {"iPhone 14", "Galaxy S23", "Xiaomi 13", "Motorola Edge 40", "Pixel 7"}
loja2 = {"iPhone 14", "Galaxy S23", "OnePlus 11", "Asus ROG Phone 6", "Nokia G60"}

lojas = loja1 | loja2

print("Total de modelos para escolha:")
for item in lojas:
    print(item)

print("\nModelos disponíveis em ambas as lojas:")
for item in loja1.intersection(loja2):
    print(item)