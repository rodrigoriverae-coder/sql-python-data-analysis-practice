SELECT TOP 10
    SalesOrderID,
    OrderDate,
    CustomerID,
    TotalDue
FROM Sales.SalesOrderHeader
WHERE Status = 5
ORDER BY TotalDue DESC;