import pandas as pd

csv = pd.read_csv("C:\\Users\\DK_GILBERT\\Desktop\\Práctica Python\\Pandas\\dataframe.csv")

"""
MÉTODO 'AGGGREGATE' (AGG)

El método 'agg' permite aplicar multiples funciones de agregación a un 
dataframe o a una serie. Es util para resumir y analizar datos de 
manera eficiente. Puedes aplicar funciones cómo: 'min', 'max', 'count'.
"""

#print(csv.groupby(['edad','nombre', 'apellido', 'nacionalidad']).agg(['min', 'max', 'count']))

filtrar = csv[((csv.nacionalidad == "venezolana") | (csv.nacionalidad == "ruso")) & (csv.edad > 29)]

print(filtrar)

ejemplo_groupby = csv.groupby("nacionalidad").size() #El método 'size()' es clave, te ahorra directamente el 'list' para mostrar resultados de agrupacion
print(ejemplo_groupby)

unstack = csv.groupby(['nacionalidad', 'edad']).size().unstack()
print(unstack) # El método 'unstack' permite transformar un nivel de índice en columnas, lo que facilita la visualización de los datos agrupados.