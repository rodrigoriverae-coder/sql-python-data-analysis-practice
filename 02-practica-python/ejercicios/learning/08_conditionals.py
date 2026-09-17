### Conditionals ###

my_condition = False  # False o True se escribe con la inicial mayúscula

if my_condition: # Es lo mismo que if my_condition = True:
    print('Se ejecuta la condición del if')
    
# print('La ejecución continúa')

my_condition = 5 * 5 # Ejemplo 2

#if my_condition:            # Esta parte pregunta, si la condicion es 10(segun lo escrito) dar como respuesta lo que solicitamos en print
                            # De lo contrario podemos colocar if my_condition = un numero
#    print('Se ejecuta la condición del if')

if my_condition == 10:
    print('Se ejecuta la condición del segundo if')

if my_condition > 10 and my_condition < 20:
    print('Es mayor que 10 y menor que 20')

elif my_condition == 25:
    print('Es igual a 25')

else:
    print('Es menor o igual que 10 o mayor o igual que 20 o distinto de 25')

print('La ejecución continúa')

my_string = ''

if not my_string:
    print('Mi cadena de texto es vacia')

if my_string == 'Mi cadena de textoooo':
    print('Mis cadenas de texto coinciden')



