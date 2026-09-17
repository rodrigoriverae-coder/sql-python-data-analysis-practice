import os
import pandas as pd

carpeta_actual = os.path.dirname(__file__)
entrada = os.path.join(carpeta_actual, 'pacientes.csv')
salida = os.path.join(carpeta_actual, 'pacientes_filtrado.csv')

df = pd.read_csv(entrada)
print("📋 Datos antes de limpiar:\n", df,"\n")

promedio_edad = round(df['edad'].mean(),0)

df['edad'] = df['edad'].astype(int).fillna(promedio_edad)

print("Datos limpios:\n",df,"\n")