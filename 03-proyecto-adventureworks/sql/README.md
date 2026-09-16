# Proyecto: Análisis de Ventas en AdventureWorks

## Descripción del Proyecto
Este proyecto contiene una serie de consultas realizadas en SQL Server diseñadas para responder preguntas clave sobre la parte comercial de la base de datos de AdventureWorks2025, los clientes y las tendencias de ventas de la empresa.

## Consultas y Casos de Negocio
1. **Top 10 Órdenes de Mayor Monto:** Identificación de las ventas más representativas.
2. **Top 5 Clientes Históricos:** Análisis consolidado del gasto acumulado e historial de compras por cliente.
3. **Categorización de Clientes:** Clasificación en segmentos *VIP*, *Frecuente* y *Estándar*.
4. **Participación de Orden por Cliente:** Cálculo del porcentaje de cada orden respecto al total histórico del cliente.
5. **Ventas por Producto y Categoría Mensual:** Integración de 5 tablas relacionales para el seguimiento de inventario y facturación.
6. **Tendencia Mensual:** Análisis de crecimiento o caída mensual mediante funciones de desfase de ventana.

## Tecnologías Utilizadas
* **Motor:** SQL Server (T-SQL)
* **Dataset:** AdventureWorks2025
* **Técnicas:** CTEs, Window Functions (`OVER`, `PARTITION BY`, `LAG`), Joins Múltiples, Agregaciones Complejas.
