import pandas as pd
import numpy as np

datos_gym = {
    'ID_Socio': [201, 202, 201, 204],
    'Plan': [' vip ', 'Regular', 'VIP', ' regular '],
    'Pago': ['S/.150', np.nan, 'S/.150', 'S/.100']
}
df_gym = pd.DataFrame(datos_gym)

df_gym['Plan'] = df_gym['Plan'].str.strip()
df_gym['Plan'] = df_gym['Plan'].str.upper()
df_gym['Pago'] = df_gym['Pago'].str.replace('S/.','',regex=False)
df_gym['Pago'] = pd.to_numeric(df_gym['Pago'])
df_gym['Pago'] = df_gym['Pago'].fillna(0)
df_gym = df_gym.drop_duplicates(subset = ['ID_Socio'])

print(df_gym)