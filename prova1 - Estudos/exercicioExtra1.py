import numpy as np

# Carregando dataset
dataset = np.loadtxt('prova1 - Estudos/space.csv', delimiter=";", dtype=str, encoding='utf-8')

# Colunas Num;Company Name;Location;Datum;Detail;Status Rocket; Cost;Status Mission
dataset = dataset[1:]

print(dataset[:, -1])

# Porcentagem de sucesso em missões
status = dataset[:, -1]
print(f"{100*(np.count_nonzero(status[status == "Success"]) / status.size):.2f}% de sucesso!")


# Media de gastos em missões
costs = np.char.strip(dataset[:, -2]).astype(float)
print(f"{costs[costs > 0].mean():.2f}")


# Número de missões espaciais feitas nos EUA nesse Dataset
missoes = dataset[:, 2]
print(missoes[np.char.find(missoes, "USA") != -1].size)


# Missões da SpaceX
spacex = np.char.strip(dataset[np.char.lower(np.char.strip(dataset[:, 1])) == "spacex"][:, -2]).astype(float)
print(spacex.max())


# Empresas e missões
empresas = np.unique(np.char.lower(np.char.strip(dataset[:, 1])), return_counts=True)

for name, num in zip(empresas[0], empresas[1]):
    print(name.capitalize(), num)