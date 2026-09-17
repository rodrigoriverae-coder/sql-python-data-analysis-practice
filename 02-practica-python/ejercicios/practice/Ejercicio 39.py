#Generando un archivo que podría no existir:

nombre_archivo = "inventario_secreto.txt"

try:
    # Intentamos abrir el archivo
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()
        print(contenido)
        
except FileNotFoundError:
    # Este bloque solo corre si el archivo no existe
    print(f"⚠️ Error: El archivo '{nombre_archivo}' no se encontró.")
    print("Creando un archivo vacío para evitar que el programa falle...")
    with open(nombre_archivo, "w") as f:
        f.write("") 

except Exception as e:
    # Este atrapa cualquier otro error inesperado
    print(f"Ocurrió un error inesperado: {e}")

finally:
    # Esto corre SIEMPRE, haya error o no
    print("Proceso de verificación finalizado.")