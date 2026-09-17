import pandas as pd

datos = {
    'Producto': ['Laptop', 'Mouse', 'Monitor', 'Teclado', 'Cargador'],
    'Stock': [15, 50, 8, 30, 5],
    'Precio_Soles': [3500, 80, 750, 150, 90]
}

df = pd.DataFrame(datos)

df['Valor_Total'] = df['Stock'] * df['Precio_Soles']

reponer = df[df['Stock']<10]

print(f'La nueva base de datos es: \n', df, '\n')
print("⚠️ Productos con stock bajo (menos de 10 unidades):\n")
print(reponer, '\n')

print('¡El tipo de cambio subió!\n')

df['Precio_Soles'] = df['Precio_Soles']+10
# 2. Recalcular el Valor_Total (porque el precio cambió)
df['Valor_Total'] = df['Stock'] * df['Precio_Soles']

# Ordenar TODO el DataFrame por la columna 'Valor_Total'
# ascending=False significa "De mayor a menor"
df = df.sort_values(by='Valor_Total', ascending=False)

print(f'El nuevo precio en soles es: \n',df, '\n')

comienzan_con_M = df[df['Producto'].str.startswith('M')]

print(f'Los productos que empizan con M son: \n', comienzan_con_M)

inversion_total = df['Valor_Total'].sum()

print(f"La inversión total en la tienda es de: S/.{inversion_total:.2f}\n")

print(df.dtypes['Valor_Total'])

def clasificacion(n):
    if n > 10000:
        return 'VIP'
    else:
        return 'Estándar'
    
df['Categoria'] = df['Valor_Total'].apply(clasificacion)

conteo_categorias = df.groupby('Categoria').size()

print("🏁 Reporte Final por Categorías: \n")
print(df[['Producto', 'Valor_Total', 'Categoria']]) # Solo vemos lo importante
print("\n📊 Resumen de conteo: \n")
print(conteo_categorias)

resumen_stock = df.groupby('Categoria')['Stock'].sum()

print("\n📦 Stock Total por Categoría: ", "\n")
print(resumen_stock)

