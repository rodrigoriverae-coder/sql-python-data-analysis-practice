producto = {
    "id": 101,
    "nombre": "teclado mecánico",
    "precio": 85.50,
    "stock": 12
}

producto["Total_inventario"] = producto["precio"] * producto["stock"]

print(f'El total del inventario es: ${producto["Total_inventario"]:.2f}')
print(f'Producto: {producto["nombre"].capitalize()} - Precio: $ {producto["precio"]:.2f}')