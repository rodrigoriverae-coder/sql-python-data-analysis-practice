'''
Programa que valide si una contraseña es segura o no considerando lo siguiente:
Una contraseña segura tiene:
 - Más de 8 caracteres.
 - Tiene al menos una mayúscula.
 - Tiene al menos un número.
'''
print('"Validación de contraseña"')

# Ejercicio 27

contraseña = input('Ingrese su nueva contraseña: ')
con_numeros = False
mayusculas = False

if len(contraseña) > 8:
    for i in contraseña:
        if i.isdigit():
            con_numeros = True
        if i.isupper():
            mayusculas = True
    if con_numeros and mayusculas:
        print('✅ Contraseña segura')
    else: 
        if not con_numeros:
            print('❌ Contraseña insegura: Falta un número')
        if not mayusculas:
            print('❌ Contraseña insegura: Falta una mayúscula')
else:
    print('❌ Insegura: Muy corta (mínimo 8 caracteres')