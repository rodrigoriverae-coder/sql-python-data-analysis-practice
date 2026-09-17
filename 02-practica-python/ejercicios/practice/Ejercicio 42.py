import os
import re

datos_sucios = "  juan@gmail.com ,  PROMO2024 , maria@outlook.com,  invitado , pedro@yahoo.com  "

while True:

    nombre_archivo = input('¿Cómo quieres llamar al archivo de salida?: ')

    if nombre_archivo.strip() == '':
        print('❌ Error: El nombre no puede estar vacío, ingrese un nombre para el archivo.')
        
    else:
        nombre_final = nombre_archivo + '.txt'
        print('✅ Perfecto, el nombre fue guardado con éxito.')
        break

entrada_limpia = [i.strip() for i in datos_sucios.split(',')]

try:
    with open(nombre_final,'w') as archivo_salida :
        for elemento in entrada_limpia:
            if '@' in elemento:
                archivo_salida.write(elemento + '\n')

    print(f'✅ ¡Éxito! Los correos válidos se guardaron en {nombre_final}')

    with open(nombre_final, 'r') as archivo_lectura:
        lineas = archivo_lectura.readlines()
        print("\n--- Resumen del Archivo ---\n")
        for i, linea in enumerate(lineas, 1):
            print(f"Correo {i}: {linea.strip()}")
        print(f"\n✅ Total: {len(lineas)} correos.")

except Exception as e:
    print(f'❌ Ocurrió un error al guardar: {e}')

# # El punto '.' significa "esta misma carpeta donde está mi script"
# carpeta_actual = "." 
# archivos = os.listdir(carpeta_actual)

# # print(f"\n--- Archivos encontrados en {os.getcwd()} ---\n")
# # for nombre in archivos:
# #     print(f"📄 {nombre}")                          
        
print("\nBuscando reportes de texto...\n")

encontrados_txt = 0
for nombre in os.listdir("."):
    if nombre.endswith(".txt"):
        encontrados_txt += 1
        print(f"🔍 Encontré un reporte: {nombre}")

print(f"\n✅ Total: {encontrados_txt} archivos.")

print("\n--- INICIANDO AUDITORÍA DE CORREOS ---\n")
gran_total_correos = 0
lista_maestra_correos = set() # 1. Creamos la lista vacía para acumular todo, pero si queremos
                           # que no se repitan, entonces creamos un SET ()

patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# 1. Listamos todo en la carpeta actual
for nombre in os.listdir("."):
    
    # 2. Solo nos interesan los archivos de texto
    if nombre.endswith(".txt") and nombre != "log_auditoria.txt": # Evitamos leer el propio log
        conteo_este_archivo = 0
        try:
            with open(nombre, 'r') as archivo:
                for linea in archivo:
                    correo = linea.strip()
                    if re.match(patron_email, correo):
                        lista_maestra_correos.add(correo)
                        conteo_este_archivo += 1
              
                # 3. Sumamos al contador global
                gran_total_correos += conteo_este_archivo
                print(f"🔎 Archivo: {nombre:25} | Correos: {conteo_este_archivo}")
                
        except Exception as e:
            print(f"❌ No se pudo leer {nombre}: {e}")

print("-" * 50)
print(f"📊 Resumen: {gran_total_correos} totales vs {len(lista_maestra_correos)} únicos.")
print(f"📊 REPORTE FINAL: Se encontraron {gran_total_correos} correos en total.")


with open("log_auditoria.txt", "w") as log:
    log.write(f"Auditoría realizada el: 2026-03-09\n") # Fecha actual
    log.write(f"Total de archivos procesados: {encontrados_txt}\n")
    log.write(f"Gran total de correos detectados: {gran_total_correos}\n")
    log.write(f"Total de correos únicos (filtrados): {len(lista_maestra_correos)}\n")
    log.write("-" * 30 + "\n")
    log.write("LISTA COMPLETA DE CORREOS:\n")

    # Escribimos los correos uno por uno
    for correo in lista_maestra_correos:
        log.write(f"{correo}\n")

print("\n📝 ¡Registro completo y lista de correos guardados en 'log_auditoria.txt'!")