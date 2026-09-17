### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {'Brais', 'Moure', 35}
print(type(my_other_set))


print(len(my_other_set))

my_other_set.add('MoureDev')

print(my_other_set) # Un set no es una estructura ordenada, al pedir el print salen los datos desordenados

my_other_set.add('MoureDev') # Un set no admite repetidos
print(my_other_set)

print('Moure' in my_other_set)
print('Mouri' in my_other_set)

my_other_set.remove('Moure')
print(my_other_set)

my_other_set.clear() # El clear solo elimina los datos de la variable, ya sea una lista, tupla o set.
print(len(my_other_set))

del my_other_set  # El del elimina la variable en su totalidad
#print(my_other_set) name 'my_other_set' is not defined

my_set = {'Brais', 'Moure', 35}
my_list = list(my_set)
print(my_list) # Convertir a una lista no es recomendable puesto que altera el orden del set
print(my_list[0])

my_other_set = {'Kotlin', 'Swift', 'Python'}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({'JavaScript', 'C#'})) # Pueden agregarse datos con el union, pero solo aquellos que no sean repetidos

print(my_new_set.difference(my_set)) # Se eliminan los datos de my set de la union


