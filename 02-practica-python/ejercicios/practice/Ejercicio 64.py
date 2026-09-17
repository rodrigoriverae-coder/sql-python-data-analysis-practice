costo_licencia = 1500

cantidad_usuarios = 12

impuesto = 1.18

presupuesto_maximo = 20000

subtotal = costo_licencia * cantidad_usuarios

total_final = subtotal * impuesto

if total_final <= presupuesto_maximo:
    print('Proyecto aprobado. Estamos dentro del presupuesto')
else:
    diferencia = total_final - presupuesto_maximo
    print(f'Proyecto rechazado. El costo excede el presupuesto por {diferencia:.2f} soles''\n')

print(f'El costo total del proyecto es de {total_final:.2f} soles')

