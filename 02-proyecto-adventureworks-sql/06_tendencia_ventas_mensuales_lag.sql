WITH info_ventas AS(	
	SELECT
		YEAR(OrderDate) AS Año,
		MONTH(OrderDate) AS Mes,
		CAST(SUM(TotalDue) AS DECIMAL (10,2)) AS VentasActuales
	FROM Sales.SalesOrderHeader
	WHERE status = 5
	GROUP BY YEAR(OrderDate), MONTH(OrderDate)
)
SELECT
	Año,
	Mes,
	VentasActuales,
	LAG(VentasActuales) OVER (ORDER BY Año, Mes) AS VentasMesAnterior,
	(VentasActuales - LAG(VentasActuales) OVER (ORDER BY Año, Mes)) AS Diferencia
FROM info_ventas
ORDER BY Año, Mes
