# Ejercicio Gemini: Mostrar un diccionario que tengo solo los códigos de producto que empiecen por "A" :

lista_inicial = 'A102 , B201 ,  A305, C400 , A500'

lista_limpia = [codigo.strip() for codigo in lista_inicial.split(',')]

solo_los_A = [codigo for codigo in lista_limpia if codigo.startswith('A')]

print(f"Lista final: {solo_los_A}")

nombre_archivo = "resultados_inventario.txt"

with open(nombre_archivo, 'w') as archivo:
  
    contenido_final = ", ".join(solo_los_A)
    
    archivo.write(contenido_final)

print(f"¡Trabajo terminado! Revisa el archivo: {nombre_archivo}")

