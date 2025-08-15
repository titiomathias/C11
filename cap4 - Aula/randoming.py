import numpy as np

np.random.seed(10)  # Para reprodutibilidade
arr = np.random.randint(1, 10, size=10)
print("Array aleatório:", arr)

# Retornando elementos únicos
unique_elements = np.unique(arr, sorted=False)
print("Elementos únicos:", unique_elements)
