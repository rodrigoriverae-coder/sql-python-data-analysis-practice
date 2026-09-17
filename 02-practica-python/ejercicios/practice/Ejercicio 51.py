import pandas as pd
import numpy as np # Necesitamos numpy para crear valores nulos

datos_hospital = {
    'Paciente': ['Ana', 'Beto', 'Carlos', 'Dora'],
    'Edad': [25, np.nan, 40, np.nan],
    'Ciudad': ['Lima', 'Cusco', None, 'Arequipa']
}
df_hosp = pd.DataFrame(datos_hospital)

'''df_hosp = df_hosp.isnull().sum()'''

df_hosp['Edad'] = df_hosp['Edad'].fillna(0)
df_hosp['Ciudad'] = df_hosp['Ciudad'].fillna('Desconocida')

print(df_hosp)