import matplotlib.pyplot as mat
import pandas as pd

finanzas = pd.read_csv("C:\\Users\\DK_GILBERT\\Desktop\\Práctica Python\\Matplotlib\\finanzas.csv")

grafico = finanzas.Articulo.value_counts().plot(); # Asignamos una variable para el gráfico y creamos la gráfica con el método 'plot()'
print(grafico) # Impromimos el gráfico para visualizarlo
mat.show() # El método 'show()' se utiliza para mostrar el gráfico generado.


grafico2 = finanzas.Articulo.value_counts().plot(kind="bar"); # Para crear un grafico de barras, se utiliza el método 'kind="bar"' dentro del plot()
print(grafico2)
mat.show()

grafico3 = finanzas.Articulo.value_counts().plot(kind="barh"); 
print(grafico3)
mat.show()

grafico4 = finanzas.Articulo.value_counts().plot(kind="pie"); 
print(grafico4)
mat.show()

grafico5 = finanzas.plot(kind="scatter", x='Unidades', y='Ganancia'); # Para crear un gráfico de dispersión, se utiliza el método 'kind="Scatter"' dentro del plot() y se especifica las columnas para los ejes x e y.
print(grafico5)
mat.show()

grafico6 = finanzas.Articulo.value_counts().plot(color="green", figsize=(10, 5)); # Para personalizar el gráfico, se pueden agregar parámetros como 'color' para cambiar el color de las barras y 'figsize' para ajustar el tamaño del gráfico.
print(grafico6)
mat.show()