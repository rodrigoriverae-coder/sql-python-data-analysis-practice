SELECT 
    distrito_tienda,
    id_venta,
    cantidad,
    -- Aquí va la magia:
    RANK() OVER(PARTITION BY distrito_tienda ORDER BY cantidad DESC) AS ranking_en_distrito
FROM ventas;

'''
Rank para asignar un número de clasificación (ranking) a cada fila dentro de un conjunto 
de resultados, basado en el orden de una columna específica.

El OVER sirve para definir una "ventana" o subconjunto de filas sobre el cual aplicar funciones 
analíticas o de agregación

Se usa con partition by para indicar a partir de qué se hará la separación de datos.

El ORDER BY sirve para ordenar esos datos de ranking de forma asc o desc

por último se le agrega un alias.

'''