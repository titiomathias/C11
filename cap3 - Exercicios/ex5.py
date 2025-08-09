# Médias

n = int(input("Digite o número de pessoas: "))

pessoas = []

for i in range(0, n):
    pessoa = {}
    pessoa["nome"] = input("Digite seu nome: ")
    pessoa["idade"] = float(input("Digite sua idade: "))
    pessoa["sexo"] = input("Digite seu sexo (m ou f): ")
    pessoas.append(pessoa)

# Função sum: Soma todos os itens de uma lista
# Função len: pega o número de itens de uma lista
# Função list: retorna uma lista a partir de um objeto iterável (string, tupla, outros)
# função map: percorre uma lista executando uma função sobre cada item da mesma e retorna um objeto map com os itens

print("Média de idade do grupo: ", sum(list(map(lambda x: x["idade"], pessoas)))/len(pessoas))
print("Mulheres com menos de 20 anos: ", len(list(x for x in pessoas if x["idade"] < 20 and x["sexo"] == "f")))