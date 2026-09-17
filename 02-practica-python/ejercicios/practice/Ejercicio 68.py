taller = [
    {"trabajo": "Afinación", "instrumento": "Bajo", "precio_usd": 50, "listo": True},
    {"trabajo": "Limpieza", "instrumento": "Guitarra", "precio_usd": 30, "listo": False},
    {"trabajo": "Cambio de cuerdas", "instrumento": "Piano", "precio_usd": 100, "listo": True},
    {"trabajo": "Electrónica", "instrumento": "Bajo", "precio_usd": 80, "listo": True}
]
tipo_cambio = 3.75

def generar_reporte(lista_de_trabajos):

    reporte_local = []

    for item in lista_de_trabajos:
        if item['listo']:
            nombre_inst = item['instrumento']
            tarea = item['trabajo']
            precio_soles = item['precio_usd'] * tipo_cambio
            mensaje = f"{nombre_inst}: {tarea} terminado. Costo: {precio_soles:.2f} soles."
            reporte_local.append(mensaje)
    return reporte_local

