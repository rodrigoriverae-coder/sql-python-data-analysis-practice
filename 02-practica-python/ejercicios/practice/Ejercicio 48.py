import pandas as pd

datos_gym = {
    'ID': [101, 102, 103, 101, 104, 102],
    'Nombre': ['Ana', 'Benito', 'Carmen', 'Ana', 'Daniel', 'Benito'],
    'Asistencias': [12, 5, 8, 12, 15, 5]
}

df_gym = pd.DataFrame(datos_gym)

df_gym['Es_Duplicado'] = df_gym.duplicated(keep=False).replace({True: 'Sí', False: 'No'})

print(df_gym)
print("-" * 30)

df_limpio = df_gym.drop(columns=['Es_Duplicado']).drop_duplicates()

print("✨ Tabla final limpia (solo registros únicos):")
print(df_limpio)