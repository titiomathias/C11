import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = x * 2

x2 = np.array([1, 2, 3, 4, 5])
y2 = x2 ** 2

plt.plot(x, y, marker='s', linestyle='dotted', color='red', linewidth=2, markersize=5)
plt.plot(x2, y2, marker='s', linestyle='dotted', color='green', linewidth=2, markersize=5)
plt.title("Meu primeiro gráfico")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.show()