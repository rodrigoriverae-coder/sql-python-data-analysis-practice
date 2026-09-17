# Programa que valide si un número es primo o no:

def es_primo(n):
    if n <= 1:
        return 'No es primo'
    for i in range(2, n):
        if n % i == 0:
            return 'No es primo'
    return 'Es primo'

for i in range(-10, 101):
    print(i, '', es_primo(i))
