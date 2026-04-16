import pandas as pd
import matplotlib.pyplot as plt
import os
import openpyxl as pxl # Para trabajar con archivo excel.


"""Crea un sistema que permita analizar los datos de un archivo CSV.
El sistema debe permitir al usuario seleccionar el archivo CSV que desea analizar."""

# Paso 1: Crear la clase AnalisisDatos.
# Paso 2: Crear un método para cargar el archivo CSV.
# Paso 3: 

class AnalisisDatos:
    def __init__(self, archivo, datos):
        self.archivo = archivo
        self.datos = datos
        
    def cargar_datos(self):
        self.archivo = input("Ingrese el nombre del archivo CSV que desea analizar:")
        self.datos = pd.read_excel(self.archivo)
        

            
if __name__ == "__main__": # Punto de entrada del programa.
            
    datos = AnalisisDatos(archivo='', datos='')
    datos.cargar_datos()
            
        