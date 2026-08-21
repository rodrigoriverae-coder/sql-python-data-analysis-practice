WITH reporte_base AS (
select
	p.id_producto,
	p.nombre_prod,
	coalesce (sum(v.cantidad),0) as total_unidades_vendidas,
	round(coalesce (sum(P.precio*V.cantidad),0),2) as ingreso_total
from productos as P
left join ventas as V
on P.id_producto=V.id_producto
group by p.id_producto, p.nombre_prod
order by p.id_producto
)
SELECT * FROM reporte_base WHERE ingreso_total = 0;