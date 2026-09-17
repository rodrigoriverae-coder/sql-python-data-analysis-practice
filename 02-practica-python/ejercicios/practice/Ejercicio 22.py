# Ejercicio 22

registro_alumnos = {}

while True:
    print("\n--- 🎓 SISTEMA DE GESTIÓN ESCOLAR ---")
    print("1. Añadir/Actualizar alumno")
    print("2. Mostrar todos los alumnos")
    print("3. Salir")
    
    opcion = input("Selecciona una opción (1-3): ")

    if opcion == "1":
        nombre = input("Introduce el nombre del alumno: ").capitalize()
        apellido = input("Introduce el apellido del alumno: ").capitalize()
        while True:
            nota = float(input(f"Introduce la nota de {nombre}: "))
            if 0 <= nota <= 20:
                break  # Salimos del bucle while porque la nota es correcta
            else:
                print("❌ Error: La nota debe estar entre 0.00 y 20.00. Inténtalo de nuevo.")
                
        # Lógica Extra: Verificar si ya existe
        if nombre in registro_alumnos:
            confirmar = input(f"El alumno {nombre} {apellido} ya existe con nota {registro_alumnos[nombre]}. ¿Actualizar? (s/n): ")
            if confirmar.lower() == 's':
                registro_alumnos[nombre] = nota
                print("Nota actualizada correctamente.")
            else:
                print("No se realizaron cambios.")
        else:
            registro_alumnos[nombre] = nota
            print(f"Alumno {nombre} {apellido} registrado con éxito.")

    elif opcion == "2":
        if not registro_alumnos:
            print("El registro está vacío.")
        else:
            print("\n--- LISTA DE ALUMNOS ---")
            for nombre, nota in registro_alumnos.items():
                # Usamos .items() para obtener llave y valor al mismo tiempo
                print(f"• Alumno: {nombre} • Apellido: {apellido} | Nota: {nota}")

    elif opcion == "3":
        print("Saliendo del sistema... ¡Hasta pronto!")
        break # Rompe el bucle while True
    
    else:
        print("Opción no válida, intenta de nuevo.")


