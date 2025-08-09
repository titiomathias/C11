dicionario = {
    "nome": "Goku",
    "raca": "Saiyajin",
    "idade": 38,
    "sexo": "masculino"
}

# Add
dicionario['poder'] = 8001
dicionario['filhos'] = ["Gohan", "Goten", "Chichi", "Pan"]

# Update
dicionario["idade"] = 45

# Delete
del dicionario["sexo"]


print(dicionario)