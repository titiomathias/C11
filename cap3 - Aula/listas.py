lista = ["Satoru Gojo", "Ryomen Sukuna", "Yuji Itadori", "Yuta Okotsu", "Zaraki"]

print("Lista original: ", lista)

# adicionando
lista.append("Hanami")
lista.insert(3, "Maki Zenin")

print("Nova lista: ", lista)

# Editando
lista[2] = "Aoi Todo"

# Excluindo
lista.remove("Satoru Gojo")
lista.pop()
del lista[1]

print("Lista modificada: ", lista)