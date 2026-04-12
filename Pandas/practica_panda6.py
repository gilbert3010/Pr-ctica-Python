import pandas as pd

"""
MÉTODO 'Head()'

El método "Head" permite ver las primeras filas de un dataframe.
Entre el parentesis 'Head(5)', podmos indicar el numeros de filas
que queremos ver.
"""

csv = pd.read_csv("C:\\Users\\DK_GILBERT\\Desktop\\Práctica Python\\Pandas\\dataframe.csv")
print(csv.head()) # Por defecto muestra las primeras 5 filas del dataframe.

""""MÉTODO 'Tail()'

El método 'Tail()', al igual que el método 'Head()', permite ver los últimos
registros o filas de un dataframe.
"""
# Ejemplo:
print(csv.tail()) # Por defecto muestra las 5 útilmas filas del dataframe.

"""MÉTODO 'INFO()'

El método 'Info()', es una función que nos permite conocer la información
básica de un dataframe, cómo el número de filas, columnas, tipos de dtaos
y si hay valores nulos.
"""

print(csv.info()) # Devuelve la información básica del dataframe.