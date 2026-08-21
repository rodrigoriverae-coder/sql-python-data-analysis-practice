WITH ventas_mensuales AS (
    SELECT 
        to_char(DATE_TRUNC('month', v.fecha),'tmMonth') AS mes,
        SUM(p.precio * v.cantidad) AS ingreso_total
    FROM ventas v
    JOIN productos p ON v.id_producto = p.id_producto
    GROUP BY 1
)
SELECT 
    mes,
    ingreso_total,
    LAG(ingreso_total) OVER(ORDER BY mes) AS ingreso_mes_anterior,
    ingreso_total - LAG(ingreso_total) OVER(ORDER BY mes) AS diferencia
FROM ventas_mensuales;

'''
Si salen null es que no hubo registros en el mes anterior. Para la parte financiera es
 correcto qe vaya null, pero para gerencia o reportes podría cambiarse a ceros usando coalesce
'''