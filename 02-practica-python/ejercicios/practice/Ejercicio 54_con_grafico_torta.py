import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot') 

datos_finales = {
    'Producto': [' Laptop ', 'Mouse', ' Monitor', 'Laptop ', 'Teclado'],
    'Venta_USD': [1200, 25, np.nan, 1200, 80],
    'Fecha': ['2023-05-01', '2023-05-02', '2023-06-10', '2023-05-01', '2023-06-15']
}
df = pd.DataFrame(datos_finales)

df['Producto']= df['Producto'].str.strip().drop_duplicates()
df['Venta_USD'] = df['Venta_USD'].fillna(300)
df['Fecha'] = pd.to_datetime(df['Fecha'])
df['Mes'] = df['Fecha'].dt.month_name()
reporte = df.groupby('Mes')['Venta_USD'].sum()

print(f'Reporte final de ventas por mes: \n', reporte)

# 1. Crear el gráfico

# autopct='%1.1f%%' sirve para mostrar el porcentaje automáticamente dentro de la tarta
reporte.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'])

plt.title('Distribución de Ventas por Mes')
plt.ylabel('') # Quitamos la etiqueta 'Venta_USD' del costado para que se vea limpio
plt.show()
