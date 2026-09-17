saldo = 4500

def desea_continuar():
    while True:
        respuesta = input('\n¿Desea realizar alguna otra operación (Sí/No)? ').lower()
        
        if respuesta == 'no':
            return True  # Orden de salir
        elif respuesta == 'si' or respuesta == 'sí':
            return False # Orden de continuar
        else:
            print("❌ Chucha no sabes leer papito? ENTIENDE! Sí o no animal!.")

while True:
    print("\n--- 🎓 BANCO TU MAMÁ LA MONTA ---")
    print('1. Consultar saldo.')
    print('2. Ingresar dinero:')
    print('3. Retirar dinero:')
    print('4. Salir.')

    opcion = input("Selecciona una opción (1-4): ")

    if opcion == '1':
        print(f'Usted cuenta con S/.{saldo} en su cuenta.')
        if desea_continuar():
            print('Gracias por su preferencia.')
            break

    elif opcion == '2':
        while True:
           try:
            dinero_ingresado = float(input('Ingrese la cantidad a depositar: S/. '))
            if dinero_ingresado < 20:
                print('El monto ingresado debe ser como mínimo 20 soles.')
            else:
              saldo += dinero_ingresado
              print(f'Su depósito se realizó con éxito. Su nuevo saldo es: S/. {saldo}')
              break
           except ValueError:
                print('Por favor ingrese una cantida válida, de lo contrario presione cancelar operación.')
        if desea_continuar():
            print('Gracias por su preferencia.')
            break

    elif opcion == '3':
        while True:
           try:
            retiro = float(input('Digite el monto solicitado: S/. '))
            if saldo < retiro:
                print(f'Saldo insuficiente. Su saldo actual es: S/. {saldo}')
            elif retiro <= 0:
               print('Monto inválido.')
            else:
               saldo -= retiro
               print(f'Retiro exitoso. Saldo restante: S/. {saldo:.2f}')
               break
           except ValueError:
              print('Ingrese una cantidad válida')
        if desea_continuar():
            print('Gracias por su preferencia.')
            break
    elif opcion == '4':
        print("Gracias por su preferencia")
    else:
        print('Una tarea tenías cojudo, váyase a la misma mierda')