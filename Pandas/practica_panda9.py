import pandas as pd

csv = pd.read_csv("C:\\Users\\DK_GILBERT\\Desktop\\Práctica Python\\Pandas\\dataframe.csv")

"""
MÉTODO 'LOC[]'

el método 'loc[]' se utiliza para acceder a filas y columnas específicas
en un dataframe utilizando etiquetas. Esto es util para filtrar datos basado
en condiciones específicas.
"""
print(csv.set_index("nacionalidad", inplace=False))
# Ejemplo: Filtrar datos donde la nacionalidad es 'ruso'.
print(csv.loc[csv.nacionalidad == "ruso"])

"""
MÉTODO 'ILOC[]'

el método 'iloc[]' se utiliza para acceder a filas y columnas específicas
en un dataframe utilizando índices enteros en lugar de etiquetas. Esto
es util para filtrar datos basado en la posición de las filas y columnas.
"""

# Ejemplo: Acceder a las primeras 3 filas del dataframe.
print (csv.iloc[0:3])

"""
MËTODO 'groupby()'

Él método 'groupby()' se utiliza para agrupar filas y columnas en específico
permitiendo sí ver en una lista toda la información del dataframe que se agrupó.
"""
print(csv.groupby("nacionalidad")) # Aquí se aplica el método groupby() en este caso en la nacionalidad y muestra el siguiente mensaje "<pandas.api.typing.DataFrameGroupBy object at 0x000002B0C7330590>"

print(list(csv.groupby("nacionalidad"))) # Para tener un resultado más gráfico, se imprime una lista primeramente para obtener cómo resultado toda la información que proporciona el método al dataframe.

for group_key, group_value in csv.groupby("nacionalidad"):
    print(group_key)
    print(group_value)