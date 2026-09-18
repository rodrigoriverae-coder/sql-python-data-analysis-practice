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

df['Producto'] = df['Producto'].str.strip()
df = df.drop_duplicates()
df['Venta_USD'] = df['Venta_USD'].fillna(300)
df['Fecha'] = pd.to_datetime(df['Fecha'])
df['Mes'] = df['Fecha'].dt.month_name()
reporte = df.groupby('Mes')['Venta_USD'].sum()

print(f'Reporte final de ventas por mes: \n', reporte)

# 1. Crear el gráfico
# kind='bar' para barras, color puede ser el que quieras
reporte.plot(kind='bar', color='skyblue', edgecolor='black')

# 2. Personalizar (Ponerle etiquetas)
plt.title('Ventas Totales por Mes')
plt.xlabel('Meses del Año')
plt.ylabel('Dólares (USD)')
plt.xticks(rotation=45) # Para que los nombres de los meses no se choquen

# 3. ¡Mostrarlo al mundo!
plt.show()