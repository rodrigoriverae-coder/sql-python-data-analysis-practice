calificaciones_estudiantes = {
    "Ana": [14, 16, 18],
    "Carlos": [10, 12, 11],
    "Sofía": [17, 19, 20],
    "Luis": [8, 9, 10]  # Sin ceros a la izquierda
}

def calculo_promedios(diccionario):
    # 1. Creamos un diccionario vacío para guardar los resultados
    promedio_estudiantes = {}
    
    # 2. Recorremos el diccionario usando .items() para obtener nombre y notas
    for estudiante, notas in diccionario.items():
        # 3. Calculamos el promedio: la suma de sus notas dividida entre la cantidad de notas
        promedio = round(sum(notas) / len(notas),2)
        
        # 4. Guardamos el resultado en el nuevo diccionario
        promedio_estudiantes[estudiante] = promedio
        
    # 5. Retornamos el diccionario completo
    return promedio_estudiantes

# Llamamos a la función y guardamos el resultado
resultado = calculo_promedios(calificaciones_estudiantes)
print(resultado)