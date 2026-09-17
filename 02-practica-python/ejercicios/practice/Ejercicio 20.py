# Ejercicio 20

carrito = [{'nombre':'Pera', 'precio' : 2.00}, 
           {'nombre':'Fresa', 'precio' : 4.00}, 
           {'nombre':'Plátano', 'precio' : 1.00}
           ]
precio_finalillo = 0
for producto in carrito:
    precio_finalillo += producto['precio']
    print(f'{producto['nombre']}: ${producto['precio']}')
print(f'--- Total a pagar: ${precio_finalillo} ---')