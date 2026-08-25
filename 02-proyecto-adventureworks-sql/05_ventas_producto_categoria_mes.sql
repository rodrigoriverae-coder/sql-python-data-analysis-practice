SELECT
	sod.ProductID,
	p.Name,
	pc.Name AS CategoriaProducto,
	SUM(sod.OrderQty) AS UnidadesVendidas,
	CAST(SUM(sod.LineTotal) AS DECIMAL (10,2)) AS VentasTotales,
	YEAR(so.OrderDate) AS Año_orden,
	MONTH(so.OrderDate) AS Mes_orden
FROM Sales.SalesOrderDetail sod
JOIN Production.Product p
ON sod.ProductID = p.ProductID
JOIN Sales.SalesOrderHeader so
ON sod.SalesOrderID = so.SalesOrderID
JOIN Production.ProductSubcategory psc
ON p.ProductSubcategoryID = psc.ProductSubcategoryID
JOIN Production.ProductCategory pc
ON psc.ProductCategoryID = pc.ProductCategoryID
WHERE status = 5
GROUP BY sod.ProductID, p.Name, pc.Name, YEAR(so.OrderDate), MONTH(so.OrderDate)
ORDER BY YEAR(so.OrderDate), MONTH(so.OrderDate)
