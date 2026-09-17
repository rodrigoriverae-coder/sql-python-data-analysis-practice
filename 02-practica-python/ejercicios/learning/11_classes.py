### Classes ###

class MyEmptyPerson: # Los nombres de las clases se escriben en mayúsculas cada letra inicial
    pass 

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = 'Sin alias'):
        self.full_name = f'{name} {surname} ({alias})'

    def walk (self):
        print(f'{self.full_name} Está caminando')

my_person = Person('Brais', 'Moure')

print(my_person.full_name)
my_person.walk()

my_other_person = Person('Brais', 'Moure', 'MoureDev')
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = 'PepeToño Masías (El loco)' # Este es un experimiento que muestra que podemos cambiar los valores originales por otros.
print(my_other_person.full_name)

my_other_person.full_name = 666 # Incluso podemos cambiar el valor por un número entero...
print(my_other_person.full_name)

