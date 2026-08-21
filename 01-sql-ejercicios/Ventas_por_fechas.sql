SELECT 
    id_venta,
    fecha,
    EXTRACT(YEAR FROM fecha) AS año,
    EXTRACT(MONTH FROM fecha) AS mes,
    EXTRACT(DAY FROM fecha) AS dia,
    CASE EXTRACT(DOW FROM fecha)
        WHEN 0 THEN 'Domingo'
        WHEN 1 THEN 'Lunes'
        WHEN 2 THEN 'Martes'
        WHEN 3 THEN 'Miércoles'
        WHEN 4 THEN 'Jueves'
        WHEN 5 THEN 'Viernes'
        ELSE 'Sábado'
    END AS dia_semana
FROM ventas;

-- Esto sirve para agrupar todas las ventas de diferentes días POR MES


SELECT 
    DATE_TRUNC('month', v.fecha) AS mes_reporte,
    SUM(p.precio * v.cantidad) AS ingreso_mensual
FROM ventas v
JOIN productos p ON v.id_producto = p.id_producto
GROUP BY 1
ORDER BY 1;