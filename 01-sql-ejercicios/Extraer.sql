SELECT 
    nombre_prod,
    LEFT(nombre_prod, POSITION(' ' IN nombre_prod) - 1) AS categoria_primaria
FROM productos;

'''
Position da la posición del espacio dentro de un nombre especificado en una columna. 
Por ejemplo: mouse inalámbrico, la posición sería 6 ya que ahí se encuentra el espacio.
Al colocar LEFT, indicamos que queremos CORTAR el nombre considerando una longitud de posición=6.
La estructura de la función left es columna y longitud.
'''

