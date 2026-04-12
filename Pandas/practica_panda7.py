import pandas as pd

"""
MÉTODO 'Values_counts()'

el método 'Values_counts()' es una función que nos permite contar la
cantidad de veces que aparece cada valor en una columna específica de 
un dataframe. Es util para entender la distribución de los datos y detectar
valores únicos o categorías en una columna.
"""

csv = pd.read_csv("C:\\Users\\DK_GILBERT\\Desktop\\Práctica Python\\Pandas\\dataframe.csv")
#print(csv.nombre.value_counts())

"""
Otra forma de trabajar con la informacion con la funcion 'value_count()'
es es utilizar la variable 'ascendig' y 'dropna' para ordennar los
resultados de forma ascendente u descendente, y para incluir o excluir
los valores nulos en el conteo.
"""

#print(csv.edad.value_counts(ascending=True, dropna=False))

"""
MÉTODO 'Sort_values()'

El método 'sort_values()' es una función que nos permite
ordenar los datos de un dataframe según uno o más columnas.
Podemos específicar el orden de la ordenación (ascendente o decendente)
y también podemos ordenar por multiples clumnas, lo que es útil para
organizar los datos de manera más compleja.
"""
print(csv.sort_values(by=['nombre', 'edad']))
