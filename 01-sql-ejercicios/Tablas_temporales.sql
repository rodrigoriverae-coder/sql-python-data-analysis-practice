SELECT 
    distrito_tienda, 
    total_vendido
FROM (
    -- Esta es la "tabla temporal" que creamos al vuelo
    SELECT distrito_tienda, SUM(cantidad) AS total_vendido
    FROM ventas
    GROUP BY distrito_tienda
) AS mi_tabla_resumen -- En Postgres, es obligatorio ponerle un nombre (alias)
WHERE total_vendido > 5;

--También se coloca dentro del from los join
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