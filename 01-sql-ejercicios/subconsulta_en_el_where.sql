select
nombre_prod,
precio
from Productos
where precio > (SELECT avg(precio) FROM PRODUCTOS);