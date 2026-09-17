lecturas = [18, 22, -5, 20, 19, -1, 25, 21]

lecturas_validas = []
errores = []

for i in lecturas:
    if i >= 0:
        lecturas_validas.append(i)
    else:
        errores.append(i)
print(lecturas_validas)
print(errores)
print(f'Se encontraron {len(errores)} errores en la base de datos.\n')