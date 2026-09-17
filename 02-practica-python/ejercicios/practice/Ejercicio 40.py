# Evaluando errores en caso de ingresar strings en lugar de ints:

while True:
    try:
        # 1. Intentamos la conversión
        dato = input("Por favor, ingresa un número para el código: ")
        numero = int(dato) 
        print(f"✅ ¡Perfecto! El número {numero} ha sido procesado.")
        break

    except ValueError:
        # 2. Si el usuario escribió letras, entramos aquí
        print("❌ Error: Eso no parece un número válido.")
        print("Asegúrate de no usar letras ni símbolos.")

    except Exception as e:
        # 3. Por si pasa algo que no imaginamos
        print(f"Ocurrió algo inesperado: {e}")

print("Continuando con el resto del programa...")