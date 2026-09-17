def calcular_comision(monto_venta, porcentaje):
    resultado =f'{(monto_venta * porcentaje) / 100:.2f}'
    return resultado

# Llamada a la función
pago = calcular_comision(1500, 10)
print(pago)