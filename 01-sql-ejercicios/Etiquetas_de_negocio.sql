WITH ventas_etiquetadas AS (
    SELECT 
        CASE 
            WHEN (p.precio * v.cantidad) > 4000 THEN '⭐ PREMIUM'
            WHEN (p.precio * v.cantidad) BETWEEN 1000 AND 4000 THEN '📦 ESTÁNDAR'
            WHEN (p.precio * v.cantidad) > 0 AND (p.precio * v.cantidad) < 1000 THEN '📉 VOLUMEN'
            WHEN (p.precio * v.cantidad) = 0 THEN '🎁 REGALO / PROMO'
            ELSE '⚠️ REVISAR'
        END AS etiqueta_negocio,
        (p.precio * v.cantidad) AS monto
    FROM ventas v
    JOIN productos p ON v.id_producto = p.id_producto
)
SELECT 
    etiqueta_negocio,
    COUNT(*) AS cantidad_ventas,
    SUM(monto) AS total_dinero
FROM ventas_etiquetadas
GROUP BY etiqueta_negocio
ORDER BY total_dinero DESC nulls last;

'''
Para cuando quisieramos etiquetas las ventas y saber qué cantida de ventas y qué monto hay 
relacionado a cada categoría creada con el case when.
'''
