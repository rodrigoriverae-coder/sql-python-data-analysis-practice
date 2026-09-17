instrumento = {
    "nombre": "Bajo Eléctrico",
    "marca": "Fender",
    "precio_usd": 800,
    "en_stock": True
}

tipo_de_cambio = 3.75

print(instrumento["nombre"],instrumento["marca"])

instrumento['precio_pen'] = instrumento["precio_usd"] * tipo_de_cambio

instrumento["en_stock"]= False

print(instrumento)