import pandas as pd

csv = pd.read_csv("C:\\Users\\DK_GILBERT\\Desktop\\Práctica Python\\Pandas\\dataframe.csv")

print(csv.groupby(['edad','nombre', 'apellido', 'nacionalidad']).agg(['min', 'max', 'count']))