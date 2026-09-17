# Otra forma de hacer busqueda de secuencias:

import ast

entrada_lista = input('Ingrese la lista: ')
entrada_secuencia = input('Ingrese la secuencia a buscar: ')

lista = ast.literal_eval(entrada_lista)
secuencia = ast.literal_eval(entrada_secuencia)

def buscar_secuencia(lista, secuencia):
    n = len(secuencia)
    return any(lista[i:i+n] == secuencia for i in range(len(lista)-n+1))

print(buscar_secuencia(lista, secuencia))
