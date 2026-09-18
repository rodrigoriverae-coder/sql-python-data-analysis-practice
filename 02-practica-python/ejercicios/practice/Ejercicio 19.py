# Ejercicio 19

# Ejercicio 19

contraseña = 'Yigoyigo1'
con_numeros = False
mayusculas = False

if len(contraseña) >= 8:
    for i in contraseña:
        if i.isdigit():
            con_numeros = True
        if i.isupper():
            mayusculas = True

    if con_numeros and mayusculas:
        print('✅ Contraseña segura')
    else:
        if not con_numeros:
            print('❌ Insegura: Falta un número')
        if not mayusculas:
            print('❌ Insegura: Use al menos una mayúscula')
else:
    print('❌ Insegura: Muy corta (mínimo 8 caracteres)')