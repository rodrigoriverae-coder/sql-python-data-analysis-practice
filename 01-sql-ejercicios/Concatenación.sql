SELECT 
    id_venta,
    distrito_tienda || ' - ' || nombre_prod AS referencia_envio
FROM ventas v
JOIN productos p ON v.id_producto = p.id_producto;