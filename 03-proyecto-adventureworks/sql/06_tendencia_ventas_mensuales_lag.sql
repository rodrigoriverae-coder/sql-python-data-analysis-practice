WITH info_ventas AS (
    SELECT
        YEAR(OrderDate) AS Año,
        MONTH(OrderDate) AS Mes,
        CAST(SUM(TotalDue) AS DECIMAL(10,2)) AS VentasActuales
    FROM Sales.SalesOrderHeader
    WHERE Status = 5
    GROUP BY
        YEAR(OrderDate),
        MONTH(OrderDate)
),
ventas_con_lag AS (
    SELECT
        Año,
        Mes,
        VentasActuales,
        LAG(VentasActuales) OVER (ORDER BY Año, Mes) AS VentasMesAnterior
    FROM info_ventas
)
SELECT
    Año,
    Mes,
    VentasActuales,
    VentasMesAnterior,
    VentasActuales - VentasMesAnterior AS Diferencia,
    CAST(
        (VentasActuales - VentasMesAnterior)
        / NULLIF(VentasMesAnterior, 0)
        AS DECIMAL(10,4)
    ) AS VariacionMensual
FROM ventas_con_lag
ORDER BY Año, Mes;