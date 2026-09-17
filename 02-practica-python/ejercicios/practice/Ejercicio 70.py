import pandas as pd
import numpy as np

datos_sucios = {
    'ID_Cliente': [101, 102, 103, 101, 105],
    'Nombre': ['  carlos', 'ANA ', ' mArIa', '  carlos', 'pedro'],
    'Email': ['Carlos@Gmail.com', 'ana@outlook.com', 'MARIA@yahoo.com', 'Carlos@Gmail.com', 'pedro@gmail.com'],
    'Edad': [28, np.nan, 34, 28, np.nan]
}
df = pd.DataFrame(datos_sucios)

df = df.drop_duplicates(subset=['ID_Cliente'])
df['Nombre'] = df['Nombre'].str.strip().str.capitalize()
df['Email'] = df['Email'].str.lower()
mediana = df['Edad'].median()
df['Edad'] = df['Edad'].fillna(mediana)
print(df)