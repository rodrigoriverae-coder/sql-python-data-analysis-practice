### Tuples ###

my_tuple = tuple() 
my_other_tuple = () # También podemos crear una tupla vacía utilizando paréntesis.

my_tuple = (35, 1.77, 'Brais', 'Moure', 'Brais')
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count('Brais'))
print(my_tuple.index('Moure')) # Nos indica el número de index o posición del elemento en la lista
print(my_tuple.index('Brais')) # También sirve para listas

#my_tuple[1] = 1.80 #La idea es cambiar el 1.77 por 1.80 pero una tupla es INMUTABLE no puede cambiarse

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple) # Cambiamos el tipo
print(type(my_tuple))

my_tuple[4] = 'MoureDev' # Modificamos el o los datos
my_tuple.insert(1, 'Azul') # Agregamos el o los datos
my_tuple = tuple(my_tuple) # En un caso atípico puede darse que tenemos que cambiar un dato.(Si es tupla no habría por qué cambiar el dato, pero supongamos que se da)
print(my_tuple)
print(type(my_tuple))

#del my_tuple[2] tuple' object doesn't support item deletion. Las tuplas no se modifican

del my_tuple
#print(my_tuple) NameError: name 'my_tuple' is not defined. Al borrar la tupla la variable no está definida


