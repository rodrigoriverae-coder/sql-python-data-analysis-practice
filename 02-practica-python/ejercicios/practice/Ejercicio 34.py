# # Convertir el primer carácter en mayúscula:

palabra = input('Ingrese la palabra: ')

def operacion(n):
    return n[0].upper() + n[1:].lower()

resultado = operacion(palabra)

print(f'Resultado: {resultado}')