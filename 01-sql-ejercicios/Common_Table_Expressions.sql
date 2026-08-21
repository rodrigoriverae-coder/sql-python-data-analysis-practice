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
Es un conjunto de resultados temporal y con nombre definido mediante la cláusula WITH. 
Actúa como una tabla virtual reutilizable durante la ejecución de una sola consulta 
(SELECT, INSERT, UPDATE o DELETE), mejorando la legibilidad y organización de SQL complejo 
sin ocupar espacio físico en disco.
'''


WITH ventas_detalle AS (
    SELECT 
        p.id_producto,
        p.nombre_prod,
        v.distrito_tienda
    FROM productos p
    LEFT JOIN ventas v ON p.id_producto = v.id_producto
)
SELECT DISTINCT nombre_prod
FROM ventas_detalle
WHERE id_producto NOT IN (
    SELECT id_producto 
    FROM ventas 
    WHERE distrito_tienda = 'San Miguel'
);