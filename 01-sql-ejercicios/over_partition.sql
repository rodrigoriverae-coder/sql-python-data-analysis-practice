SELECT 
    distrito_tienda,
    id_venta,
    (cantidad * 100.0 / SUM(cantidad) OVER(PARTITION BY distrito_tienda)) AS porcentaje_del_distrito
FROM ventas;

-- La consulta se hace dentro del select 

SELECT 
    v.distrito_tienda,
    p.nombre_prod,
    (p.precio * v.cantidad) AS monto,
    ROW_NUMBER() OVER(
        PARTITION BY v.distrito_tienda 
        ORDER BY (p.precio * v.cantidad) DESC
    ) AS ranking_en_distrito
FROM ventas v
JOIN productos p ON v.id_producto = p.id_producto;