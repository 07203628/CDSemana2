### Ejercicio 8: Arquitectura de Almacenamiento

## 1. ¿Qué es Data Lake?
Un **Data Lake** (Lago de Datos) es un repositorio centralizado que permite almacenar todos los datos, tanto estructurados como no estructurados, a cualquier escala. 

* **Características:**
    * Guarda los datos en su formato original (raw data) sin necesidad de definirlos primero.
    * Es altamente escalable y económico.
    * Ideal para Big Data, Machine Learning y análisis predictivo.
* **Analogía:** Es como un cuerpo de agua en estado natural donde los datos fluyen y se quedan ahí hasta que alguien decide cómo usarlos.

## 2. ¿Qué es un Data Warehouse?
Un **Data Warehouse** (Almacén de Datos) es un sistema diseñado para el análisis y la elaboración de informes de datos procesados.

* **Características:**
    * Los datos están altamente estructurados y organizados (esquema definido).
    * Se alimenta de datos provenientes de sistemas transaccionales y otras fuentes.
    * Optimizado para consultas rápidas de negocio y Business Intelligence (BI).
* **Analogía:** Es como un almacén de botellas de agua purificada, etiquetadas y ordenadas en estanterías listas para su consumo.

## 3. Diferencias entre OLAP y OLTP
Estas siglas definen cómo se procesan los datos según el objetivo del sistema.

| Característica | OLTP (Online Transactional Processing) | OLAP (Online Analytical Processing) |
| :--- | :--- | :--- |
| **Objetivo** | Operaciones diarias (insertar, actualizar). | Análisis y toma de decisiones. |
| **Datos** | Datos actuales y detallados. | Datos históricos y agregados. |
| **Velocidad** | Respuesta inmediata (milisegundos). | Consultas complejas que pueden tardar segundos/minutos. |
| **Ejemplo** | Un cajero automático o una compra en Amazon. | Un reporte de ventas anuales por región. |

## 4. ¿Qué es ETL?
**ETL** son las siglas de **Extract, Transform, and Load** (Extraer, Transformar y Cargar). Es el proceso tradicional de integración de datos.

1. **Extract (Extraer):** Se recopilan datos de diversas fuentes (bases de datos SQL, archivos logs, APIs).
2. **Transform (Transformar):** Se limpian, filtran y convierten los datos para que cumplan con el formato del destino (ej. normalizar fechas, quitar duplicados).
3. **Load (Cargar):** Se insertan los datos ya procesados en el destino final, usualmente un Data Warehouse.