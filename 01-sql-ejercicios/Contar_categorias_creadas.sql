--Metodo 1:

select tipo_precio, count(*) from (
	select
	nombre_prod,
	precio,
	case 
		when precio > 1000 then 'Caro' 
		else 'Barato' 
		end as tipo_precio	
	from Productos 
	order by nombre_prod) as consulta_precios
group by tipo_precio

--Metodo 2: 

SELECT 
    CASE WHEN precio > 1000 THEN 'Caro' ELSE 'Barato' END AS tipo_precio, 
    COUNT(*)
FROM productos
GROUP BY tipo_precio; -- ¡Mucho más corto!

