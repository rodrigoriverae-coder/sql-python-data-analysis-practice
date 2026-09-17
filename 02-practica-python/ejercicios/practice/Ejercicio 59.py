stock = {"Laptops": 5, "Mouses": 0, "Teclados": 12, "Monitores": 2, "Cables": 0}

for producto, cantidad in stock.items():
    if producto == "Teclados":
        continue
    if cantidad == 0:
        print(f"ALERTA: {producto} agotado. Realizar pedido inmediato.")
    if 1 <= cantidad < 5:
        print(f"AVISO: {producto} con stock bajo ({cantidad} unidades).")

