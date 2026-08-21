SELECT nombre_prod, precio
FROM productos
WHERE id_producto IN (SELECT id_producto FROM ventas);