SELECT top 10
	SalesOrderID,
	OrderDate,
	CustomerID,
	TotalDue
FROM Sales.SalesOrderHeader
WHERE Status = 5
AND TotalDue > 1000
ORDER BY TotalDue DESC;