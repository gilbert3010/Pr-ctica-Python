import pandas as pd

#MÉTODO 'read_excel'
"""
read_excel es un método de 'to_excel' disponible
para Dataframes que permite la lectura del contenido
de --ficheros excel--. como el método 'to_excel', es 
necesario indicar la ruta dle fichero y la pestana que queremos
leer.

Argumentos: Cómo el método 'to_excel', es necesario indicar
la ruta y el fichero ya demás la pestana que queremos leer.
"""
#Ejemplos:

df_read = pd.read_excel('C:Direccion/del/archivo_excel.xlsx', 'pestana')
print(df_read)

# También podemos indicar el índice de la hoja que queremos leer
df_read = pd.read_excel('C:Direccion/del/archivo_excel.xlsx', 1)
print(df_read)

# Podemos ver el resto de argumentos disponibles utilizando el signo de interrogación.
#print(pd.read_excel?)