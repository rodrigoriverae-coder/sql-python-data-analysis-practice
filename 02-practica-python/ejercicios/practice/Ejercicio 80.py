def obtener_comision_dinamica(monto_venta):
    if monto_venta > 3000:
        pago_final = monto_venta * 0.15  # Corregido a 0.15
    elif monto_venta >= 1000:
        pago_final = monto_venta * 0.10  # Corregido a 0.10
    else:                             # Si no es mayor a 3000 ni >= 1000, por defecto es menor a 1000
        pago_final = monto_venta * 0.05  # Corregido a 0.05
        
    return round(pago_final, 2)       # Redondeamos directo en el retorno

# Llamadas limpias sin necesidad de usar round afuera
print(obtener_comision_dinamica(500))
print(obtener_comision_dinamica(2000))
print(obtener_comision_dinamica(4000))