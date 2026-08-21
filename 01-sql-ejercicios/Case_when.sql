SELECT 
    distrito_tienda,
    CASE
        WHEN EXTRACT(MONTH FROM fecha) = 1 THEN 'Enero'
        WHEN EXTRACT(MONTH FROM fecha) = 2 THEN 'Febrero'
        WHEN EXTRACT(MONTH FROM fecha) = 3 THEN 'Marzo'
        WHEN EXTRACT(MONTH FROM fecha) = 4 THEN 'Abril'
        WHEN EXTRACT(MONTH FROM fecha) = 5 THEN 'Mayo'
        WHEN EXTRACT(MONTH FROM fecha) = 6 THEN 'Junio'
        WHEN EXTRACT(MONTH FROM fecha) = 7 THEN 'Julio'
        WHEN EXTRACT(MONTH FROM fecha) = 8 THEN 'Agosto'
        WHEN EXTRACT(MONTH FROM fecha) = 9 THEN 'Septiembre'
        WHEN EXTRACT(MONTH FROM fecha) = 10 THEN 'Octubre'
        WHEN EXTRACT(MONTH FROM fecha) = 11 THEN 'Noviembre'
        WHEN EXTRACT(MONTH FROM fecha) = 12 THEN 'Diciembre'
        ELSE 'Otro'
    END AS mes, 
    SUM(cantidad) AS total_vendido
FROM ventas
GROUP BY distrito_tienda, mes
HAVING total_vendido > 5
ORDER BY distrito_tienda, mes;

--La idea es hacer un case when por cada mes para poder tener una tabla que muestre el 
nombre del mes si al extraer el mes se tienen número (lo cual sí sucede)

--Ejercicio 2 

SELECT 
    nombre_prod, 
    CASE 
        WHEN precio IS NULL OR precio = 0 THEN 'Sin precio'
        ELSE precio::text
    END AS nuevos_precios
FROM Productos;

