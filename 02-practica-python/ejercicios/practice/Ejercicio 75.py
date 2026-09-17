usuarios = [" juan ", "MARTA", " pEro ", " Lucia"]

usuarios_limpios = []

for i in usuarios:
    x = i.strip().capitalize()
    usuarios_limpios.append(x)

print(usuarios_limpios)