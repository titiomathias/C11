import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dfPaises = pd.read_csv("cap6 - Aula/paises.csv", delimiter=";")

print(dfPaises)

dfMaioresPaisses = dfPaises.nlargest(6, "Area (sq. mi.)")
print(dfMaioresPaisses["Country"])

plt.scatter(dfMaioresPaisses["Country"], dfMaioresPaisses["GDP ($ per capita)"], color="red", marker="s", s=100)
plt.xlabel("Países")
plt.ylabel("GDP ($ per capita)")
plt.show()

