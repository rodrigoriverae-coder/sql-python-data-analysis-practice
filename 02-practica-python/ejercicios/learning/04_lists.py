### Lists ###

my_list = list()    # De esta forma se indica que es una lista
my_other_list = []  # De esta forma también

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, 'Brais', 'Moure'] # El tamaño de la lista debe ser igual que el de los nombres que le demos luego.
                 
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30)) # Cuenta cuántas veces se repite el dato solicitado
#print(my_other_list[4]) IndexError
#print(my_other_list[-5]) IndexError

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

print(my_list + my_other_list)
#print(my_list - my_other_list) 

my_other_list.append('MoureDev') # Agrega datos al final de la lista
print(my_other_list)

my_other_list.insert(1,'Rojo') # Agrega datos donde le indiquemos según posición
print(my_other_list)

my_other_list[1] = 'Azul' # Reemplaza datos según una posición
print(my_other_list)

my_other_list.remove('Azul')
print(my_other_list)

my_list.remove(30)
print(my_list)

print(my_list.pop()) # Remueve el último dato de la lista.  Si indicamos un número, se remueve el dato asignado según posición
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print( my_list)

del my_list[2] # Elimina el elemento sin reservarlo. El pop lo reserva 
print(my_list)

my_new_list = my_list.copy() # Antes de borrar una lista podemos utilizar esto para mantenerla reservada en su totalidad

my_list.clear() # Elimina por completo la lista
print(my_list)
print(my_new_list)

my_new_list.reverse() # Da la vuelta a la lista
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:3]) # Para indicar que nos muestra el dato que está entre la posición 1 y 3

my_list = 'Hola Python'
print(my_list)
print(type(my_list))