codigos = [14, 25, 36, 47, 58, 69, 80, 91]

pares = 0
impares = 0

for i in codigos:
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'El total de números pares es: {pares}')
print(f'El total de números impares es: {impares}')