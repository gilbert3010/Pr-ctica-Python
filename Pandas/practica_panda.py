import pandas as pd

dataframe = pd.read_csv('C:/Users/DK_GILBERT/Desktop/Práctica Python/Pandas/dataframe.csv')

while True:
    print("Que datos quieres ver?:\n1. Nombre\n2. Apellido\n3. Edad\n4. Nombre y Apellido\n5. Carrera y Nacionalidad\n6. Tabla completa\n7. Salir")
    opcion = input("ingrese un número: ")
    if opcion == "1":
        print(dataframe["nombre"])
    elif opcion == "2":
        print(dataframe["apellido"])
    elif opcion == "3":
        print(dataframe["edad"])
    elif opcion == "4":
        print(dataframe[["nombre", "apellido"]])
    elif opcion == "5":
        print(dataframe[["carrera", "nacionalidad"]])
    elif opcion == "6":
        print(dataframe)
    elif opcion == "7":
        print("Saliendo...")
        break
    else:
        print("Numero invalido.")
        
#print(dataframe[["nombre", "apellido", "edad"]])
#print(dataframe)