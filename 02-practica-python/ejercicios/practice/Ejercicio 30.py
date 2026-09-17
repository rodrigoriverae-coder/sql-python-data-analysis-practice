# Programa que pida dos números al usuario y de como resultado 
# la operación matemática que el usuario pida:

numero_1 = float(input('Ingrese el primer número: '))
numero_2 = float(input('Ingrese el segundo número: '))

print('''Elija la operación a realizar: 
        1. Suma
        2. Resta
        3. Multiplicación
        4. División
        5. Potenciación
        6. Radicación
''')
opcion = int(input('Ingrese el número de opción: '))

def operacion(n):
    if n == 1:
        return numero_1 + numero_2
    elif n == 2:
        return numero_1 - numero_2
    elif n == 3:
        return numero_1 * numero_2
    elif n == 4:
        return numero_1 / numero_2 if numero_2 == 0 else "Error: División por cero"
    elif n == 5:
        return numero_1 ** numero_2
    else:
        return numero_1 ** (1/numero_2)

print(f'El resultado es: {operacion(opcion):.2f}')