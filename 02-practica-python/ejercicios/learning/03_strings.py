### Strings ###

my_string = 'Mi string'
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + ' ' + my_other_string)

my_new_line_string = 'Este es un string\ncon salto de lìnea'
print(my_new_line_string)

my_tab_string = '\tEste es un string con tabulación'
print(my_tab_string)

my_scape_string = '\\tEste es un string \\n escapado'
print(my_scape_string)

# Formateo

name, surname, age = 'Brais', 'Moure', 35

print('Mi nombre es {} {} y mi edad es {}'.format(name, surname, age))
print('Mi nombre es %s %s y mi edad es %s' %(name, surname, age))
print('Mi nombre es ' + name + ' ' + surname + ' y mi edad es ' + str(age)) #Esta es la forma más trabajosa 
print(f'Mi nombre es {name} {surname} y mi edad es {age}') #Aquí se da formato con la f al inicio

# Desempaquetado de caracteres
language = 'python'
a, b, c, d, e, f = 'Python'
print(a)
print(b)

# Division

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones

print(language.capitalize()) #Primera letra mayúscula
print(language.upper()) #Todas mayúsculas
print(language.count('t'))
print(language.isnumeric())
print('1'.isnumeric())
print(language.lower()) #Todas minúsculas
print(language.lower().islower())
print(language.startswith('Py'))  # Py no es igual que py por lo que es importante saber cómo escribimos el valor de la variable language

