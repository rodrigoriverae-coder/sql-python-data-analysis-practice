temperaturas = [22, 25, 10, 28, 5, 24, 26]

clima_real = []

for n in temperaturas:
    if n <= 15:
        print(f'Error en registro: {n}')
    else:
        clima_real.append(n)

print(clima_real)