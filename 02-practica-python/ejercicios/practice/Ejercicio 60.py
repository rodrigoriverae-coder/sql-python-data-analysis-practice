pedidos = [["laptop", "mouse"], ["laptop", "monitor"], ["mouse", "mouse"]]

ventas_totales = {}

for pedido in pedidos:        # Este entra en cada lista: ["laptop", "mouse"]
    for producto in pedido:   # Este entra en cada palabra: "laptop", luego "mouse"
        
        if producto in ventas_totales:
            ventas_totales[producto] += 1
        else:
            ventas_totales[producto] = 1

print(ventas_totales)