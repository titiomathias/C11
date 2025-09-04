import numpy as np

# Exercício 1

arr1 = np.ones(8)
arr2 = np.random.randint(1, 10, size=8)
arr3 = arr1 + arr2

print(arr1)
print(arr2)
print(arr3.sum())

if arr3.sum() >= 40:
    print(arr3.reshape(4, 2))
else:
    print(arr3.reshape(2, 4))
