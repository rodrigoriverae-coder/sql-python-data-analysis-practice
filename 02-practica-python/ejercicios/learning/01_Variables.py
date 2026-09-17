#Variable

my_string_variable = 'My String variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

#Concatenación en variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)
print('Este es el valor de:', my_bool_variable)

#Algunas Funciones del sistema
print(len(my_string_variable))

#Variables en una sola linea ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = 'Brais','Moure', 'MoureDev', 35
print('Me llamo', name, surname, ', mi edad es', age, 'y mi alias es', alias  )

#Inputs
""""
name = input('Cuál es tu nombre: ')
age = input('Cuántos años tienes? ')

print(name)
print(age)
""" 

#Cambiamos su tipo
name = 35
age = 'Brais'

print(name)
print(age)

#¿Forzamos el tipo?
address: str = 'Mi dirección'
address = 32

print(type(address))