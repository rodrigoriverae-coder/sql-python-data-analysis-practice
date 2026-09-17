# Ejercicio que combina evaluación de error y bucle:

# --- PASO 1: Bucle de entrada segura ---
while True:
    try:
        entrada = input("¿De qué número quieres los múltiplos?: ")
        numero_base = int(entrada) # Intentamos convertir
        
        tope_entrada = input("¿Hasta qué número quieres llegar?: ")
        tope = int(tope_entrada)
        
        if numero_base <= 0 or tope <= 0:
            print("⚠️ Por favor, ingresa números mayores a cero.")
            continue # Reinicia el bucle si los números no tienen sentido
            
        break # Si todo salió bien, rompemos el bucle y avanzamos
        
    except ValueError:
        print("❌ Error: Ingresaste letras. Por favor, usa solo números enteros.")

# --- PASO 2: Procesamiento de datos ---
# Generamos la lista usando el rango con 'paso'
multiplos = [x for x in range(numero_base, tope + 1, numero_base)]

# --- PASO 3: Guardado en archivo ---
try:
    with open("mis_multiplos.txt", "w") as archivo:
        # Convertimos la lista a texto para guardarla
        resultado_texto = ", ".join(map(str, multiplos))
        archivo.write(resultado_texto)
    print(f"\n✅ ¡Éxito! Se han guardado {len(multiplos)} múltiplos en 'mis_multiplos.txt'.")

except Exception as e:
    print(f"❌ No se pudo guardar el archivo: {e}")