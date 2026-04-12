import pandas as pd

"""
MÉTODO 'Shape'

El método 'shape' permite conocer las filas y columnas de un dataframe.
Es una función muy útil para entender la estructura de los datos que estamos manejando.
"""

csv = pd.read_csv("C:\\Users\\DK_GILBERT\\Desktop\\Práctica Python\\Pandas\\dataframe.csv")
print(csv.shape) # Devuelve una tupla con el número de filas y columnas del dataframe.
print(csv.shape[0]) # filas
print(csv.shape[1]) # columnas

