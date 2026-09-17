import pandas as pd
import numpy as np

datos_ventas = {
    'Factura': [501, 502, 502, 504, 505],
    'Monto_USD': ['$150', '$200', '$200', np.nan, '$450'],
    'Estado': ['entregado ', ' CANCELADO', 'entregado ', 'entregado', 'PENDIENTE']
}
df_ventas = pd.DataFrame(datos_ventas)

df_ventas = df_ventas.drop_duplicates(subset = ['Factura'])
df_ventas['Estado'] = df_ventas['Estado'].str.strip().str.capitalize()
df_ventas['Monto_USD'] = df_ventas['Monto_USD'].str.replace('$','')
df_ventas['Monto_USD'] = df_ventas['Monto_USD'].fillna(0)


print(df_ventas)