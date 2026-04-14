import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patheffects as patheffects

# Leer el archivo CSV con el separador correcto
finanzas = pd.read_csv("C:\\Users\\DK_GILBERT\\Desktop\\Práctica Python\\Matplotlib\\ejemplo_mat.csv", sep=';')

# Eliminar filas con valores vacíos
finanzas = finanzas.dropna()

print(finanzas['Elon Mosk'].head())

fig, ax = plt.subplots(figsize=(15, 8))

ax.plot(finanzas['Elon Mosk'], 
        label='Elon Mosk', 
        lw=2, 
        color='red',
        path_effects=[patheffects.SimpleLineShadow(), patheffects.Normal()])

ax.set_xlabel('Índice')
ax.set_ylabel('Valor')
ax.set_title('Evolución de Elon Mosk')
ax.legend()
ax.grid(True, alpha=0.3)

ax.plot(finanzas['Bill Gate'], 
        label='Bill Gate', 
        lw=2, 
        color='blue',
        path_effects=[patheffects.SimpleLineShadow(), patheffects.Normal()])

ax.set_xlabel('Índice')
ax.set_ylabel('Valor')
ax.set_title('Evolución de Bill Gate')
ax.legend()
ax.grid(True, alpha=0.3)

plt.show()