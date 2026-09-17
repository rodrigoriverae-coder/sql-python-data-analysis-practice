ventas_usd = [
    {"producto": "Teclado", "precio": 25},
    {"producto": "Monitor", "precio": 200},
    {"producto": "Mouse", "precio": 15},
    {"producto": "Laptop", "precio": 1200}
]
tipo_de_cambio = 3.75  # 1 USD = 3.75 PEN

ventas_soles = []

for venta in ventas_usd:
    nombre = venta['producto']
    precio_pen = venta['precio'] * tipo_de_cambio
    if  precio_pen < 1000:
        nueva_venta = {'producto':nombre,'precio':precio_pen}
    else:
        nueva_venta = {'producto':nombre,'precio':precio_pen,'categoria':'Venta Grande'}

    ventas_soles.append(nueva_venta)

print(ventas_soles)




