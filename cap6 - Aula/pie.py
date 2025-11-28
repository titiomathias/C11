import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dfPaises = pd.read_csv("cap6 - Aula/paises.csv", delimiter=";")

dfNoCoast = dfPaises[dfPaises["Coastline (coast/area ratio)"] == 0]

qtNoCoast = len(dfNoCoast)
qtCoast = len(dfPaises) - qtNoCoast

plt.pie([qtNoCoast, qtCoast], labels=["No Coast", "Coast"], autopct="%1.1f%%", colors=["lightblue", "lightgreen"])
plt.title("Proporção de países com e sem litoral")
plt.show()