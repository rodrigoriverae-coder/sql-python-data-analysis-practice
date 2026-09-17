contraseña = "" # Inicializamos vacía para que entre al bucle

while contraseña != "python123":
    contraseña = input('Ingrese la contraseña: ')
    
    if contraseña == "salir":
        print("Proceso cancelado")
        break
    
    if contraseña == "python123":
        print("Acceso concedido")
    else:
        print("Error, intente nuevamente")