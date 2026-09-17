# Programa que calcule la tabla de multiplicar del 0 al 12 de cualquier número entero dado por el usuario:

print('"Tabla de multiplicar"')

num_ingresado = int(input('Introduzca el número solicitado: '))

def tabla_multiplicar(n):
    for i in range (0, 13):
        print(f'{n} * {i} = {n*i}')

tabla_multiplicar(num_ingresado)