import pandas as pd

datos_ventas = {
    'Fecha': ['2023-01-01', '2023-02-15', '2023-03-10'],
    'Monto': [500, 300, 450]
}
df_ventas = pd.DataFrame(datos_ventas)

df_ventas['Fecha'] = pd.to_datetime(df_ventas['Fecha'])

df_ventas['Mes'] = df_ventas['Fecha'].dt.month_name()

df_ventas_filtrado = df_ventas[df_ventas['Mes'] == 'January']

print(f'Los nuevos datos son: \n', df_ventas_filtrado, '\n')

'''
Se está convirtiendo las fechas que son textos a formato fecha con la función month(que da 
numeros del 1 al 12) o month_name que da los nombres (en inglés)
'''
