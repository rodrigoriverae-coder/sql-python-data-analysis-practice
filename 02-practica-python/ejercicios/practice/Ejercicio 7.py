# Ejercicio 7

mi_cumple = (1,'diciembre', 1992)

try:
    mi_cumple[2] = 2024
    print('Se pudo cambiar el dato)')
except TypeError as error:
    print('No se pudo cambiar el dato', 'y el error es este:', error)