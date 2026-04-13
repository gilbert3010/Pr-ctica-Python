import pandas as pd


"""
Cómo filtrar datos en un dataframe 
"""
csv = pd.read_csv("C:\\Users\\DK_GILBERT\\Desktop\\Práctica Python\\Pandas\\dataframe.csv")

#print(csv.nacionalidad == "ruso")

#if csv.nombre[0] == "gilberto" and csv.apellido[0] == "meneses":
#   print(csv[["nombre", "apellido"]])
#else:
#    print("Datos no encontrados.")
    
print(csv[csv.nacionalidad == "ruso"])

"""
MÉTODO 'Set_index'

El método 'set_index' se utiliza para establecer una columna específica
cómo el índice del dataframe. Esto puede ser util para organizar y acceder
a los datos de manera más eficiente.
"""
print(csv.set_index("nacionalidad", inplace=False))

"""
MÉTODO 'Sort_index'

El método 'sort_index' se utiliza para ordenar el dataframe según el 
índice establecido. esto es útil para organizar los datos de manera
ascendente o decendente.
"""

print(csv.nacionalidad.sort_index(inplace=False))