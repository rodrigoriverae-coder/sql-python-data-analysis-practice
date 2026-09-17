inventario = [
    {"nombre": "Laptop", "categoria": "Tecnología", "stock": 5},
    {"nombre": "Mouse", "categoria": "Tecnología", "stock": 25},
    {"nombre": "Silla", "categoria": "Hogar", "stock": 3},
    {"nombre": "Escritorio", "categoria": "Hogar", "stock": 2},
    {"nombre": "Teclado", "categoria": "Tecnología", "stock": 12}
]

def filtrar_por_stock_critico(lista_inventario, limite):
    # 1. Creamos la lista vacía dentro de la función
    inventario_filtrado = []
    
    # 2. Recorremos cada producto de la lista con un bucle for
    for producto in lista_inventario:
        # 3. Comparamos el stock del producto actual con el límite
        if producto["stock"] <= limite:
            # 4. Si cumple, guardamos su nombre en la lista
            inventario_filtrado.append(producto["nombre"])
            
    # 5. Retornamos la lista resultante
    return inventario_filtrado

# Llamamos a la función pasando el inventario y el límite (por ejemplo, 10)
resultado = filtrar_por_stock_critico(inventario, 10)
print(resultado)