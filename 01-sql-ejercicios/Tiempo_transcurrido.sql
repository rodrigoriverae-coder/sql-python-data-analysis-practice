SELECT 
    id_venta,
    fecha,
    CURRENT_DATE AS hoy,
    CURRENT_DATE - fecha AS dias_transcurridos
FROM ventas;