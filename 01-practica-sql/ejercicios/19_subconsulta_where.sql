-- Productos cuyo precio es mayor al precio promedio de todos los productos.

SELECT
    nombre_prod,
    precio
FROM productos
WHERE precio > (
    SELECT AVG(precio)
    FROM productos
);

