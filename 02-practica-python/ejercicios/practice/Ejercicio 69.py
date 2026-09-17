cuerdas = [
    {"nombre": "Bajo Fender", "precio_usd": 800, "limpio": True},
    {"nombre": "Guitarra Gibson", "precio_usd": 1200, "limpio": False}
]

teclados = [
    {"nombre": "Piano Yamaha", "precio_usd": 3000, "limpio": True},
    {"nombre": "Sintetizador Korg", "precio_usd": 500, "limpio": True}
]

def analizar_stock(lista_inventario):
    
    resultado = []
    
    for instrumento in lista_inventario: # Recorremos la lista que entre
        if instrumento['limpio']: # Si el instrumento actual está limpio
            # Accedemos al NOMBRE del instrumento actual, no a la lista entera
            nombre = instrumento['nombre']
            precio = instrumento['precio_usd']
            
            terminados = {'nombre': nombre, 'precio_usd': precio}
            resultado.append(terminados)
            
    return resultado

# LLAMADAS (Aquí ocurre la magia)
reporte_cuerdas = analizar_stock(cuerdas)
reporte_teclados = analizar_stock(teclados)

print("Cuerdas limpias:", reporte_cuerdas)
print("Teclados limpios:", reporte_teclados)