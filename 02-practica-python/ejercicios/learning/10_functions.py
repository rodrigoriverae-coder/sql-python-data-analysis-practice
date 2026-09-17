### Functions ###

def my_function ():
    print('Esto es una funcion')

my_function ()

def sum_two_values (fisrt_value, second_value):
    print(fisrt_value + second_value)

sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values('5','7')
sum_two_values(1.4, 5.2)

def sum_two_values_with_return (first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name (name, surname):
    print(f'{name} {surname}')

print_name(surname = 'Moure', name = 'Brais')

def print_name_with_default (name, surname, alias = 'Sin alias'):
    print(f'{name} {surname} {alias}')

print_name_with_default('Brais', 'Moure')

def print_texts(*text):
    print(text)

print_texts('Hola', 'Python', 'MoureDev')

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print_upper_texts('Hola', 'Python', 'MoureDev')

