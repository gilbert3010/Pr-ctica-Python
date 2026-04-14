import matplotlib.pyplot as mat
import pandas as pd

finanzas = pd.read_csv("C:\\Users\\DK_GILBERT\\Desktop\\Práctica Python\\Matplotlib\\ejemplo_mat.csv")
print(finanzas['Elon Mosk'].head())

fig, ax = mat.subplots(figsize=(15,8))
ax.plot(finanzas['Elon Mosk'], label='Elon Mosk', lw=2, color='red',
        path_effects=[mat.simplelineshadow(), mat.Normal()])


mat.show();

