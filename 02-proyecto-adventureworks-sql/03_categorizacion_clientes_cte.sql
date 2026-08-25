WITH categoria AS (
	SELECT
		CustomerID,
		CASE WHEN SUM(TotalDue) >= 500000 THEN 'VIP'
		WHEN SUM(TotalDue) BETWEEN 100000 AND 499999 THEN 'Frecuente'
		ELSE 'Estándar'
		END AS CategoriaCliente
	FROM Sales.SalesOrderHeader
	WHERE status = 5
	GROUP BY CustomerID	
)
SELECT TOP 15
	so.CustomerID,
	CONCAT_WS(' ', p.FirstName, p.MiddleName, p.LastName) AS NombreCliente,
	ROUND(SUM(so.TotalDue), 2) AS MontoTotal,
	ct.CategoriaCliente
FROM Sales.SalesOrderHeader so
JOIN Sales.Customer c
ON so.CustomerID = c.CustomerID
JOIN Person.Person p
ON c.PersonID = p.BusinessEntityID
JOIN categoria ct
ON so.CustomerID = ct.CustomerID
GROUP BY so.CustomerID, FirstName, p.MiddleName, p.LastName, ct.CategoriaCliente
ORDER BY ROUND(SUM(so.TotalDue), 2) desc

	