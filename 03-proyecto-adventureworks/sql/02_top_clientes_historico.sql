SELECT TOP 5
    so.CustomerID,
    CONCAT_WS(' ', p.FirstName, p.MiddleName, p.LastName) AS NombreCliente,
    ROUND(SUM(so.TotalDue), 2) AS MontoTotal,
    COUNT(*) AS TotalOrdenes
FROM Sales.SalesOrderHeader so
JOIN Sales.Customer c
    ON so.CustomerID = c.CustomerID
JOIN Person.Person p
    ON c.PersonID = p.BusinessEntityID
WHERE so.Status = 5
GROUP BY
    so.CustomerID,
    p.FirstName,
    p.MiddleName,
    p.LastName
ORDER BY MontoTotal DESC;