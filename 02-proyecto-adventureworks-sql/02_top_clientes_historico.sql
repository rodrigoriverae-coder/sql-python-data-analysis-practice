SELECT top 5
	so.CustomerID,
	CONCAT_WS(' ', p.FirstName, p.MiddleName, p.LastName) AS NombreCliente,
	ROUND(SUM(so.TotalDue), 2) AS MontoTotal,
	COUNT (*) AS TotalOrdenes
FROM Sales.SalesOrderHeader so
JOIN Sales.Customer c
ON so.CustomerID = c.CustomerID
JOIN Person.Person p
ON c.PersonID = p.BusinessEntityID
WHERE status = 5
GROUP BY so.CustomerID, FirstName, p.MiddleName, p.LastName
ORDER BY ROUND(SUM(so.TotalDue), 2) desc
