inventario = [
    {"id": 101, "nombre": "teclado", "precio": 85.50, "stock": 12},
    {"id": 102, "nombre": "mouse", "precio": 25.00, "stock": 0},
    {"id": 103, "nombre": "monitor", "precio": 320.00, "stock": 5},
    {"id": 104, "nombre": "audífonos", "precio": 60.00, "stock": 0}
]


for producto in inventario:
    if producto["precio"] <= 60:
        producto["precio"] *= 1.10

for producto in inventario:
    producto["precio"] = f'{producto["precio"]:.2f}'

print(inventario)