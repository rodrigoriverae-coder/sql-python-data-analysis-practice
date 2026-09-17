# Programa qu muestre el nuevo salario de un empleado considerando un incremento del x%:

salario_base = int(input('Ingrese su salario actual: '))
porcentaje = int(input('Ingrese el incremento: '))

def calculo_salario(salario, tasa):
    return salario * (tasa/100) + salario

resultado = calculo_salario(salario_base, porcentaje)

print(f'Su nuevo salario es: {resultado:.2f}')


# Programa qu muestre el nuevo salario de un empleado considerando un incremento del x%:

salario_base = int(input('Ingresa tu webada: '))
porcentaje = int(input('Cuánto quieres aumentar oe: '))

calculo_salario = lambda salario, tasa : salario * (tasa/100) + salario

resultado = calculo_salario(salario_base, porcentaje)

print(f'Ya ya tu nueva plata son: {resultado:.2f} soles vete y no jodas')