import pandas as pd

alumnos = {
    'Nombre': ['  luis', 'MARIA', '  pedro'],
    'Nota': [18, 12, 15]
}
df = pd.DataFrame(alumnos)

df['Nombre'] = df['Nombre'].str.strip().str.capitalize()

df['Puntos_Extra'] = df['Nota'] + 2

df_filtrado = df[df['Nota'] > 13]

print(f'Los nuevos datos son:\n', df_filtrado, '\n' )





