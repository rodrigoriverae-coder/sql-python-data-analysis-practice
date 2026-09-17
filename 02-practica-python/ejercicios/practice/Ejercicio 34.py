# Programa que devuelva el primer caracter en minuscula y el resto normal:

palabra = input('Ingrese la palabra: ')

def operacion(n):
    return n[0].upper() + n[1:].lower()

resultado = operacion(palabra)

print(f'Resultado: {resultado}')