import pandas as pd


"""
Cómo filtrar datos en un dataframe 
"""
csv = pd.read_csv("C:\\Users\\DK_GILBERT\\Desktop\\Práctica Python\\Pandas\\dataframe.csv")

#print(csv.nacionalidad == "ruso")

if csv.nombre[0] == "gilberto" and csv.apellido[0] == "meneses":
    print(csv[["nombre", "apellido"]])
else:
    print("Datos no encontrados.")