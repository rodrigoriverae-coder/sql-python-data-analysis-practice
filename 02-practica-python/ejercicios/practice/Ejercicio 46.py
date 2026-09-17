import pandas as pd

fuerza_de_ventas = {'vendedor':['Carlos','Roberto','Alfonso','Alfonso','Roberto'],
                    'monto_venta':[1200, 1700, 1500, 1500, 2450]
                    }

df = pd.DataFrame(fuerza_de_ventas)

ventas_por_vendedor = df.groupby('vendedor')['monto_venta'].sum()
analisis_estadistico = round(df.describe(),2)

print(f'Las ventas totales por cada vendedor son: {ventas_por_vendedor}','\n')
print(f'El analisis es el siguiente:{analisis_estadistico}','\n')

