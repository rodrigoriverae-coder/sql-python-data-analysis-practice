SELECT 
    P.nombre_prod, 
    COALESCE(SUM(V.cantidad * P.precio), 0) AS monto_total
FROM productos AS P
LEFT JOIN ventas AS V 
    ON P.id_producto = V.id_producto 
    AND V.distrito_tienda = 'San Miguel' -- Filtramos "durante" la unión
GROUP BY P.nombre_prod
ORDER BY monto_total DESC;

'''
Calculamos el monto total de ventas de cada producto en el distrito de San Miguel.

El filtro del distrito se coloca dentro del ON del LEFT JOIN para conservar
también los productos que no tienen ventas en San Miguel.

COALESCE permite reemplazar el resultado NULL por 0 cuando un producto no
tiene ventas que cumplan la condición.
'''
