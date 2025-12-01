import numpy as np

# Exercícios Parte 3

dataset = np.loadtxt('C:\\Users\\mathi\\OneDrive\\Documentos\\c11-exs\\NP3 - Estudos\\EX - Cap4\\space.csv', delimiter=';', dtype=object, encoding='utf-8')

# Tratando dados
dataset[1:, 0] = dataset[1:, 0].astype(int)  # ID
dataset[1:, 6] = dataset[1:, 6].astype(float)  # Cost

# Missões que deram certo
sucesso = np.sum(dataset[1:, 7] == 'Success')
print("Missões que deram certo:", sucesso/(len(dataset) - 1) * 100, "%")

# Média de gastos em uma missão espacial
# Filtrando missões
dataset = dataset[1:, :]  # Removendo cabeçalho
dataset = dataset[dataset[:, 6] != 0.0]
print("Média de gastos em uma missão espacial:", np.mean(dataset[:, 6]))


# Quantas missões foram feitas pelo EUA
country = dataset[:, 2].astype(str)
missoes_eua = np.count_nonzero(np.char.find(country, 'USA') != -1)
print("Missões feitas pelo EUA:", missoes_eua)


# Missão mais cara da SpaceX
spacex = dataset[dataset[:, 1] == 'SpaceX']
print("Missão mais cara da SpaceX:", dataset[np.argmax(spacex[:, 6])])

# Empresas e missões
empresas, contagem = np.unique(dataset[:,1], return_counts=True)
for empresa, count in zip(empresas, contagem):
    print(f"Empresa: {empresa}, Missões: {count}")

    