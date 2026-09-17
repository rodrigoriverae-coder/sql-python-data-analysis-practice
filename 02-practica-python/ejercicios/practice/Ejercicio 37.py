'''
Programa que reciba una frase y que devuelva un diccionario con la cantidad de veces que se
repite cada palabra en esa frase.
'''
#frase = 'La palabra que más se repite es la, o quizá la palabra , palabra, palabra'
def dic_contador():
    parrafo = input('Ingresa tu frase: ')

    contador = {}
    palabras = parrafo.replace(',', '').replace('.', '').lower().split()

    for i in palabras:
        if i in contador:
            contador[i] += 1
        else: 
            contador[i] = 1
        
    return contador
print(dic_contador())

