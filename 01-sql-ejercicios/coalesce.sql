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
Creamos una columna a partir de la suma de dos columnas de tablas diferentes usando JOIN
y en lugar de usar Where se usa AND dentro del JOIN porque el where arruina lo que hace el left JOIN
porque left join trae los datos hacia la izquierda incluyendo los que tienen dato 0 en este
casto ventas 0, pero si luego decir where entonces filtramos los que digan san miguel 
y si habian ventas con 0 que eran de otro distrito, desaparecerán.

Coalesce sirve para decirle a sql que si hay datos con valores NULL los reemplace con 0.

'''
