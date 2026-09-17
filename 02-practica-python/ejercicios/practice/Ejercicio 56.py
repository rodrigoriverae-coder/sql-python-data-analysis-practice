lista = list(range(1,21))

for i in lista:
    if i % 2 == 0:
        print(i)
    else: 
        print(f'{i} No es un número par')