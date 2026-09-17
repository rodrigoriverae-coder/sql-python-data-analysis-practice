'''
El reto: Crea un programa que permita gestionar gastos diarios.
    Debe permitir al usuario ingresar un gasto (nombre del artículo y precio).
    Almacena los gastos en una lista de diccionarios.
    Crea una función que calcule el total gastado.
    Crea otra función que encuentre el gasto más caro.
        Plus: Usa el módulo dates para registrar la fecha y hora exacta de cada gasto.
'''

print('--- Gestor de Gastos Diarios ---\n')

historial_gastos = [] # Aquí guardaremos los diccionarios de cada gasto

while True:
    articulo = input('Ingrese el nombre del artículo (o "salir" para terminar): ')
    if articulo.lower() == 'salir':
        break
    
    try:
        precio = float(input(f'Ingrese el precio de "{articulo}": $'))
        
        # Creamos un diccionario para este gasto específico
        gasto_actual = {"nombre": articulo, "precio": precio}
        
        # Lo añadimos a nuestra lista general
        historial_gastos.append(gasto_actual)
        
    except ValueError:
        print("Error: Por favor ingrese un número válido para el precio.")

# Ahora calculamos el total usando una lista de solo los precios
# Usamos una "list comprehension" (que tienes en tu carpeta Intermedio)
precios_solo = [gasto["precio"] for gasto in historial_gastos]
total_gastado = sum(precios_solo)

print(f"\nHas registrado {len(historial_gastos)} productos.")
print(f"El gasto total al momento es de: ${total_gastado:.2f}")

