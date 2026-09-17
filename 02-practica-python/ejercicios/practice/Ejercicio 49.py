import pandas as pd

datos_empleados = {
    'Nombre': ['  JUAN', 'elena  ', ' MarIa ', 'pedro'],
    'Sueldo': [2000, 2500, 2200, 1800]
}
df_emp = pd.DataFrame(datos_empleados)

df_emp['Nombre'] = df_emp['Nombre'].str.strip().str.capitalize()

df_emp['Nombre_Mayus'] = df_emp['Nombre'].str.upper()

print('Los nuevos datos son: \n', df_emp, '\n')

df_filtrado = df_emp[(df_emp['Sueldo']>2100) & (df_emp['Nombre'] == 'Elena')]

print('Los nuevos datos filtrados son: \n', df_filtrado, '\n')