# SQL — Análisis de ventas en AdventureWorks2025

## Descripción

Consultas realizadas en SQL Server para analizar órdenes, clientes, productos y evolución de ventas a partir de la base de datos AdventureWorks2025.

## Consultas realizadas

1. **Top 10 órdenes por monto**
   - Identificación de las órdenes con mayor `TotalDue`.

2. **Top 5 clientes históricos**
   - Análisis del monto acumulado y número de órdenes por cliente.

3. **Categorización de clientes**
   - Segmentación de clientes en VIP, Frecuente y Estándar según criterios definidos para el análisis.

4. **Participación de cada orden por cliente**
   - Cálculo de la participación de cada orden respecto al total histórico de su cliente utilizando funciones de ventana.

5. **Ventas por producto y categoría**
   - Análisis mensual de unidades vendidas y ventas por producto y categoría.

6. **Tendencia mensual de ventas**
   - Comparación de las ventas de cada mes con el mes anterior utilizando `LAG()`.

## Técnicas utilizadas

- JOIN.
- CTE.
- Funciones de agregación.
- `CASE WHEN`.
- Funciones de ventana.
- `PARTITION BY`.
- `LAG()`.
- Agrupaciones por año y mes.

## Herramientas

- SQL Server
- AdventureWorks2025

## Lenguaje

- SQL (T-SQL)