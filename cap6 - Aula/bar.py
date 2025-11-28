import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dfPaises = pd.read_csv("cap6 - Aula/paises.csv", delimiter=";")

print(dfPaises)

dfMaioresPaisses = dfPaises.nlargest(5, "GDP ($ per capita)")
print(dfMaioresPaisses["Country"])

plt.bar(dfMaioresPaisses["Country"], dfMaioresPaisses["GDP ($ per capita)"], color="blue")
plt.xlabel("Países")
plt.ylabel("GDP ($ per capita)")
plt.title("Top 5 Países por GDP per capita")
plt.show()