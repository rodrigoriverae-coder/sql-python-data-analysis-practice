# Programa que convierta dias horas minutos y segundos a segundos:

dias = int(input('Ingrese los días a convertir: '))
horas = int(input('Ingrese las horas a convertir: '))
minutos = int(input('Ingrese los minutos a convertir: '))
segundos = int(input('Ingrese los segundos a convertir: '))

conversion = lambda d, h, m, s : (d * 24 * 60 * 60) + (h * 60 * 60) + (m * 60) + s

resultado = conversion(dias, horas, minutos, segundos)

print(f'El resultado es: {resultado} segundos')