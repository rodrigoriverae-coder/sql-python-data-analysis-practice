SELECT 
    UPPER(TRIM(v.distrito_tienda)) AS distrito_limpio,
    LOWER(p.nombre_prod) AS producto_minuscula,
    LENGTH(p.nombre_prod) AS largo_nombre -- Calcula la cantidad de caracteres
FROM ventas v
JOIN productos p 
    ON v.id_producto = p.id_producto;