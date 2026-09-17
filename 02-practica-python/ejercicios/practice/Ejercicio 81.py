ventas_semana = [
    {"producto": "Laptop", "cantidad": 2, "precio_unitario": 850.0},
    {"producto": "Mouse", "cantidad": 15, "precio_unitario": 25.5},
    {"producto": "Teclado", "cantidad": 8, "precio_unitario": 45.0},
    {"producto": "Monitor", "cantidad": 4, "precio_unitario": 200.0},
    {"producto": "Mouse", "cantidad": 5, "precio_unitario": 25.5}, # Nota: El mouse se vendió en dos momentos
]

ingresos_por_producto = {}

for item in ventas_semana:
    producto = item["producto"]
    ingreso_transaccion = item["cantidad"] * item["precio_unitario"]
    if producto in ingresos_por_producto:
        ingresos_por_producto[producto] += ingreso_transaccion
    else:
        ingresos_por_producto[producto] = ingreso_transaccion  

print(ingresos_por_producto)