# Nome e peso

lista = []

for n in range(0, 3):
    pessoa = {}
    pessoa["nome"] = input("Digite seu nome: ")
    pessoa["peso"] = float(input("Digite seu peso: "))
    lista.append(pessoa)

# Para conseguir utilizar a função max, aprendi a passar o parâmetro key, que recebe uma função para comparar cada elemento da lista
# Como a lista é composta de dicionários, estou passando para ele comparar apenas o peso do item de tipo dicionário

print("Pessoa com maior peso: ", max(lista, key=lambda p: p["peso"])["nome"])
print("Pessoa com menor peso: ", min(lista, key=lambda p: p["peso"])["nome"])
