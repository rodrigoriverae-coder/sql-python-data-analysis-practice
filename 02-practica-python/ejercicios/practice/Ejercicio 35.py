# Dada una lista de enteros, determinar si la secuencia [10, 20, 30], está en algún lugar de la lista.


def list_ent(lista):
    i = 0
    while i < (len(lista)-2):
        if lista[i] == 10 and lista[i+1] == 20 and lista[i+2] == 30:
            return True
        else:
            i +=1
    return False

print(list_ent([40, 50, 10, 20, 30, 60, 41, 70]))