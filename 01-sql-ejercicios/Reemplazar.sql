SELECT 
    UPPER(REPLACE(nombre_prod, '24p', '24 PULGADAS')) AS nombre_detallado
FROM productos
WHERE nombre_prod LIKE '%Monitor%';