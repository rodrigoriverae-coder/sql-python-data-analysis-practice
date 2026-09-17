SELECT 
    distrito_tienda, 
    total_vendido
FROM (
    -- Subconsulta en FROM: crea una tabla derivada para la consulta externa
    SELECT distrito_tienda, SUM(cantidad) AS total_vendido
    FROM ventas
    GROUP BY distrito_tienda
) AS mi_tabla_resumen -- En Postgres, es obligatorio ponerle un nombre (alias)
WHERE total_vendido > 5;

-- La subconsulta puede utilizar JOIN para obtener los datos necesarios
-- antes de generar el resultado que utilizará la consulta externa.

-- Clasificar las ventas y luego contar las operaciones por categoría

SELECT 
    resumen.tipo_de_venta, 
    COUNT(*) AS total_operaciones
FROM (
    SELECT 
        CASE 
            WHEN (P.precio * V.cantidad) >= 4000 THEN 'Venta Top'
            WHEN (P.precio * V.cantidad) >= 1000 THEN 'Venta Media'
            ELSE 'Venta Económica'
        END AS tipo_de_venta
    FROM ventas V
    JOIN productos P ON V.id_producto = P.id_producto
) AS resumen
GROUP BY resumen.tipo_de_venta;