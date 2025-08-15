import numpy as np

arr1 = np.arange(1, 11)
arr2 = np.arange(10, 0, -1)

print("Array 1:", arr1)
print("Array 2:", arr2)

# Operações básicas com numpy arrays passam por broadcasting
print("Soma:", arr1 + arr2)


# Concatenação de arrays
arr_concat = np.concatenate([arr1, arr2])
print("Array Concatenado:", arr_concat)


# Operações com matrizes
mtz1 = np.array([[50, 10, 100, 60, 25, 100, 75, 80, 100]]).reshape(3, 3)
print("Matriz 1:\n", mtz1)

gastos = mtz1.sum(axis=1) 
print("Gastos em janeiro: ", gastos[0])
print("Gastos em fevereiro: ", gastos[1])
print("Gastos em março: ", gastos[2])

# Broadcasting em matrizes
print(  mtz1 / 10)
