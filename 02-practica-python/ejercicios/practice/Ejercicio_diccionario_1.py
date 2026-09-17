# archivo_info = {'nombre':'auditoria_marzo', 'formato':'txt', 'lineas':150 }

# archivo_info['lineas']=200

# print(archivo_info['nombre'])
# print(archivo_info['lineas'])

import pandas as pd

archivos_auditoria = [
    {"nombre": "ventas.txt", "correos": 10, "estado": "OK"},
    {"nombre": "usuarios.txt", "correos": 52, "estado": "OK"},
    {"nombre": "errores.txt", "correos": 0, "estado": "REVISAR"}
    ]
for i in archivos_auditoria:
    if i['estado'] == 'REVISAR':
        print(f"Alerta: El archivo {i['nombre']} necesita atención")

suma_correos = 0
for i in archivos_auditoria:
    if i["estado"] == 'OK':
        suma_correos += i["correos"]
print(suma_correos)

