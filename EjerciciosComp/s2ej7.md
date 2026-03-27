### Ejercicio 7: Tipos de Bases de Datos NoSQL
## 1. **Documentales**: MongoDB, CouchDB
* **¿Cuándo usar?:** Gestión de contenido (CMS), catálogos de e-commerce, aplicaciones con datos semi-estructurados o donde el esquema cambia frecuentemente.
* **Ventajas:** * Flexibilidad total (esquema dinámico).
    * Mapeo directo con objetos en lenguajes de programación (JSON).
    * Escalabilidad horizontal sencilla.
* **Desventajas:**
    * Mayor uso de almacenamiento por redundancia de llaves.
    * No son ideales para relaciones extremadamente complejas.

## 2. **Key-Value**: Redis, DynamoDB
* **¿Cuándo usar?:** Caché de datos, gestión de sesiones de usuario, carritos de compra o configuraciones rápidas.
* **Ventajas:**
    * Latencia extremadamente baja (muy rápidas).
    * Estructura muy simple y fácil de implementar.
* **Desventajas:**
    * No permite realizar consultas complejas sobre el contenido del valor.
    * Obliga a conocer la llave exacta para recuperar la información.

## 3. **Columnar**: Cassandra, HBase
* **¿Cuándo usar?:** Análisis de Big Data, almacenamiento de logs masivos, series temporales y sistemas de telemetría (IoT).
* **Ventajas:**
    * Alta eficiencia en la compresión de datos.
    * Lectura de columnas específicas sin leer toda la fila.
    * Escalabilidad masiva para petabytes de datos.
* **Desventajas:**
    * Escrituras más lentas que en otros modelos NoSQL.
    * Diseño rígido basado en las consultas finales (Query-driven design).

## 4. **Graph**: Neo4j
* **¿Cuándo usar?:** Redes sociales, motores de recomendación, detección de fraude y logística.
* **Ventajas:**
    * Rendimiento superior al recorrer relaciones complejas.
    * Visualización intuitiva de conexiones entre entidades.
* **Desventajas:**
    * Difíciles de escalar horizontalmente.
    * Curva de aprendizaje alta (requieren lenguajes de consulta específicos como Cypher).
