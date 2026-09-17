# Ejercicio 19

contraseña = 'Yigoyigo1'
con_numeros = False
mayusculas = False

if len(contraseña) >= 8:
    for i in contraseña:
        if i.isdigit():
            con_numeros = True
            print('❌ Insegura: Falta un número')
            break
        if i.isupper():
            mayusculas = True
            print('❌ Insegura: Use al menos una mayúscula')
            break
    if con_numeros and mayusculas:
        print('✅ Contraseña segura')
    else: 
        print('❌ Contraseña insegura')
else:
    print('❌ Insegura: Muy corta (mínimo 8 caracteres')