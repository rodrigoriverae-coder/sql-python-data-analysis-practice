ventas_usd = [
    {"producto": "Teclado", "precio": 25},
    {"producto": "Monitor", "precio": 200},
    {"producto": "Mouse", "precio": 15},
    {"producto": "Laptop", "precio": 1200}]

tipo_de_cambio = 3.75

ventas_soles = []

for venta in ventas_usd:
    nombre = venta['producto']
    precio_usd = venta['precio'] # Guardamos el original para la validación
    
    # 1. PARADA DE SEGURIDAD (Si es muy caro, nos detenemos)
    if precio_usd > 1000:
        print(f"Alerta: Venta crítica de {nombre}. Deteniendo proceso.")
        break
        
    # 2. FILTRO DE EXCLUSIÓN (Si es Mouse, lo saltamos)
    if nombre == 'Mouse':
        continue
        
    # 3. PROCESAMIENTO (Si pasó los filtros anteriores, calculamos y guardamos)
    precio_soles = precio_usd * tipo_de_cambio
    nueva_venta = {'producto': nombre, 'precio': precio_soles}
    ventas_soles.append(nueva_venta)
    
print("Reporte final de ventas en Soles:")
print(ventas_soles)