WITH ventas_mensuales AS (
    SELECT 
        DATE_TRUNC('month', v.fecha) AS mes_fecha,
        TO_CHAR(DATE_TRUNC('month', v.fecha), 'TMMonth') AS mes,
        SUM(p.precio * v.cantidad) AS ingreso_total
    FROM ventas v
    JOIN productos p 
        ON v.id_producto = p.id_producto
    GROUP BY 1, 2
)
SELECT 
    mes,
    ingreso_total,
    LAG(ingreso_total) OVER(ORDER BY mes_fecha) AS ingreso_mes_anterior,
    ingreso_total - LAG(ingreso_total) OVER(ORDER BY mes_fecha) AS diferencia
FROM ventas_mensuales
ORDER BY mes_fecha;

'''
Si el primer mes aparece con NULL en ingreso_mes_anterior, es porque no existe
un mes anterior dentro del periodo analizado.

Para un análisis financiero, mantener NULL puede ser apropiado porque no existe
un valor anterior con el cual comparar.

En algunos reportes podría utilizarse COALESCE para mostrar 0, dependiendo de
lo que se quiera comunicar.
'''