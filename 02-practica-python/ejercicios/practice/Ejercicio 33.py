# Comprobar si una palabra es palindroma 

print('"Identificador de palindromía"\n')

frase = input('Ingrese la palabra o frase a evaluar: ')

frase_limpia = frase.lower().replace(" ","")

frase_invertida = frase_limpia[::-1]

if frase_limpia == frase_invertida:
    print(f'\n✅ "{frase}" es palíndroma.')
    print(f'Al derecho: {frase_limpia}')
    print(f'Al revés:   {frase_invertida}')
else:
    print(f'\n❌ "{frase}" no es palíndroma.')


