# Programa que calcule el IGV de un producto y que muestre el valor final
# considerando un valor de IGV del 18%:

print('"Sistema de cálculo de precios"')

valor_inicial = float(input('Inserte el valor de su producto: '))

def valor_producto(valor):
    igv = 0.18 * valor
    return valor + igv

print(f'El valor final del producto es de: {valor_producto(valor_inicial)}')