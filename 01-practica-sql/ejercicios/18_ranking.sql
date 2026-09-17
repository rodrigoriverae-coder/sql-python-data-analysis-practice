SELECT 
    distrito_tienda,
    id_venta,
    cantidad,
    -- Aquí va la magia:
    RANK() OVER(PARTITION BY distrito_tienda ORDER BY cantidad DESC) AS ranking_en_distrito
FROM ventas;

'''
RANK() asigna una posición de clasificación a cada fila según el valor
indicado en ORDER BY.

OVER() define la ventana sobre la que se realiza el cálculo.

PARTITION BY divide los datos en grupos independientes. En este caso,
se genera un ranking separado para cada distrito.

ORDER BY establece el criterio utilizado para ordenar el ranking.

Si dos filas tienen el mismo valor, RANK() les asigna la misma posición
y deja un salto en la siguiente posición.

'''