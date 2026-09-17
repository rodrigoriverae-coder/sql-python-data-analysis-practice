-- 1. Definimos el CTE (La tabla temporal)
WITH resumen_distritos AS (
    SELECT distrito_tienda, SUM(cantidad) AS total_unidades
    FROM ventas
    GROUP BY distrito_tienda
)
-- 2. Ahora consultamos esa tabla que acabamos de "inventar"
SELECT * FROM resumen_distritos
WHERE total_unidades < 5;

'''
Un CTE (Common Table Expression) es un conjunto de resultados temporal
definido mediante WITH.

Funciona como una tabla virtual que puede utilizarse dentro de la
consulta principal. Permite organizar consultas complejas y hacerlas
más fáciles de leer.
'''


WITH ventas_detalle AS (
    SELECT 
        p.id_producto,
        p.nombre_prod,
        v.distrito_tienda
    FROM productos p
    LEFT JOIN ventas v 
        ON p.id_producto = v.id_producto
)
SELECT DISTINCT nombre_prod
FROM ventas_detalle vd
WHERE NOT EXISTS (
    SELECT 1
    FROM ventas v
    WHERE v.id_producto = vd.id_producto
      AND v.distrito_tienda = 'San Miguel'
);