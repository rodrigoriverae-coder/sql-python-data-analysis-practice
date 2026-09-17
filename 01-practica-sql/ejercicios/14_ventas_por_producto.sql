-- Identificar productos que no registran ventas.

WITH reporte_base AS (
    SELECT
        p.id_producto,
        p.nombre_prod,
        COALESCE(SUM(v.cantidad), 0) AS total_unidades_vendidas,
        ROUND(COALESCE(SUM(p.precio * v.cantidad), 0), 2) AS ingreso_total
    FROM productos AS p
    LEFT JOIN ventas AS v
        ON p.id_producto = v.id_producto
    GROUP BY p.id_producto, p.nombre_prod
)
SELECT *
FROM reporte_base
WHERE ingreso_total = 0
ORDER BY id_producto;