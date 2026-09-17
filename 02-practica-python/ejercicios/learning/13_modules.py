### Modules ###

import my_module

my_module.sumValue(5, 3, 1)
my_module.printValue('Hola Python!')

from my_module import sumValue, printValue

sumValue(5, 3, 1)
printValue('Hola Python')

import math # es un modulo del sistema de python que incluye operaciones que ayudan a hacer otras operaciones

print(math.pi)
print(math.pow(2, 8)) # Potencia

from math import pi as PI_VALUE

print(PI_VALUE)