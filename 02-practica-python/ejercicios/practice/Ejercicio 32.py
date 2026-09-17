'''
Programa que muestre el nivel de masa corporal (IMC) dado su peso y estatura. 
Indicar el nivel de peso así:
      < 18.50 --> bajo peso
18.50 - 24.9 --> Normal
25.00 - 29.9 --> Sobrepreso
30.00 - 34.9 --> Obesidad I
35.00 - 39.9 --> Obesidad II
40.00 - 49.9 --> Obesidad III
      > 50.0 --> Obesidad IV

IMC = pes / (estatura * estatura)
'''

print('"Caluladora de masa corporal"\n')
estatura = float(input('Ingrese su estatura en m: '))
peso = float(input('Ingrese su peso en kg: '))

calculo_imc = lambda talla, peso : peso / (talla * talla)

resultado = calculo_imc(estatura, peso)

if resultado < 18.5:
    nivel = 'bajo peso'
elif 18.5 <= resultado <= 24.9:
    nivel = 'normal'
elif 25.00 <= resultado <= 29.9:
    nivel = 'sobrepeso'
elif 30.00 <= resultado <= 34.9:
    nivel = 'Obesidad I'
elif 35.00 <= resultado <= 39.9:
    nivel = 'Obesidad II'
elif 40.00 <= resultado <= 49.9:
    nivel = 'Obesidad III'
else:
    nivel = 'Obesidad IV'


print(f'Su índice de masa corporal IMC es {nivel}, siendo el restulado: {resultado:.2f} kg/m2')
