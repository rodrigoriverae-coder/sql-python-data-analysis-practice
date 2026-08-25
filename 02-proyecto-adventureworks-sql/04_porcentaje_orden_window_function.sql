SELECT
	CustomerID,
	SalesOrderID,
	OrderDate,
	TotalDue AS MontoOrden,
	SUM(TotalDue) OVER(PARTITION BY CustomerID) AS MontoTotalCliente,
	CAST((TotalDue / (SUM(TotalDue) OVER(PARTITION BY CustomerID))) AS DECIMAL (10,4)) AS PorcentajeDelTotal
FROM Sales.SalesOrderHeader
WHERE status = 5
ORDER BY CustomerID, OrderDate
