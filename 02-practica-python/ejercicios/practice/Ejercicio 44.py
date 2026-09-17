import pandas as pd

productos = {'nombre':['pastel', 'helado', 'frap', 'pan'],
             'precio':[12, 5, 7, 3]
            }
df = pd.DataFrame(productos)

mayores_a_5 = df[df['precio'] >= 5]

print("☕ Los productos mayores a $5 son:")
print(mayores_a_5)
print("\n👀 Las primeras 2 filas son:")
print(df.head(2))
