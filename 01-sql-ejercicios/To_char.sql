SELECT 
    distrito_tienda,
    TO_CHAR(fecha, 'Month') AS mes, -- 'Month' devuelve el nombre completo
    SUM(cantidad)
FROM ventas
GROUP BY distrito_tienda, mes;


--La idea es dar la cantidad, mes y nombre de distrito sin la necesidad de usar un
 --case when por cada mes