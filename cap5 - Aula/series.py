import pandas as pd

indices = ['a', 'b', 'c']
valores = [1, 2, 3]

serie = pd.Series(data=valores, index=indices)

print(serie)
print(serie['a'])

# OPERAÇÕES ENTRE SERIES

serie2 = pd.Series({'a':10, 'b':30, 'c':60, 'd':39, 'e':100})
print(serie + serie2)
print(serie - serie2)

print(serie.add(serie2, fill_value=0))
print(serie.sub(serie2, fill_value=0))
