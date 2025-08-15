import numpy as np

# Criando numpy arrays
arr = np.array([1,2,'3'])

# Criando uma matriz 2D
mtz = np.array([[1,2,3], [4,5,6]])

print(type(arr))
print(mtz)

# Funções para estruturar numpy arrays
arr_1 = np.ones(10)
arr_0 = np.zeros(10)

# RESHAPE
mtz = arr_0.reshape(5,2)

print(mtz)

# Sem reshape
mtz2 = np.zeros((5,5))
print(mtz2)

# ARANGE

arr2 = np.arange(10, 1001, 10)
print(arr2.min())
print(arr2.max())
print(arr2.mean())
print(arr2.argmax())
print(arr2.argmin())
