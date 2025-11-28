import pandas as pd
import numpy as np

np.random.seed(10)

df = pd.DataFrame(
    index = ["A", "B", "C", "D"],
    columns=["W", "X", "Y", "Z"],
    data=np.random.randint(1,50, [4, 4])
)

print(df)

# FAZENDO SLICING COM iloc (padrão NumPy - indices numéricos)
print(df.iloc[0:2, :])
print(df.loc['A':'B', :]) # Ou df.loc[['A', 'B'], ['W', 'X', 'Y', 'Z']]