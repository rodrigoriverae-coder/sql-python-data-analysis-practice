# Programa que toma las 3 notas de un estudiante y te da la finall

print('Inserte las notas escolares del alumno: ')

def nota_escolar(n1, n2, n3):
    return ((n1 * 0.30) + (n2 * 0.30) + (n3 * 0.4))

nota_1 = float(input('Nota 1: '))
nota_2 = float(input('Nota 2: '))
nota_3 = float(input('Nota 3: '))

nota_final = nota_escolar(nota_1, nota_2, nota_3)

print(f'La nota final del curso es: {round(nota_final,2)}')