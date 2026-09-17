inventario = [
    {"id": 101, "nombre": "teclado", "precio": 85.50, "stock": 12},
    {"id": 102, "nombre": "mouse", "precio": 25.00, "stock": 0},
    {"id": 103, "nombre": "monitor", "precio": 320.00, "stock": 5},
    {"id": 104, "nombre": "audífonos", "precio": 60.00, "stock": 0}
]

productos_sin_stock = 0


for producto in inventario:
    if producto["stock"] == 0:
        print(f'Alerta: El producto {producto["nombre"].capitalize()} está agotado')
        productos_sin_stock += 1

print(f'El total de productos sin stock es de: {productos_sin_stock}')
