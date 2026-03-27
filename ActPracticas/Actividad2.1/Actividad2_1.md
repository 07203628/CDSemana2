# Actividad 2.1: Investigación de Arquitecturas de Datos

## 1. Conceptos Fundamentales

### Data Warehouse (Almacén de Datos)
Es un sistema diseñado para el análisis de datos estructurados provenientes de diversas fuentes. Sigue un enfoque de **Schema-on-Write** (el esquema se define antes de guardar los datos). Es el pilar del Business Intelligence tradicional.

### Data Lake (Lago de Datos)
Es un repositorio que almacena datos en su formato nativo (brutos), ya sean estructurados, semi-estructurados o no estructurados. Sigue un enfoque de **Schema-on-Read** (la estructura se aplica solo cuando los datos son consultados).

---

## 2. Comparativa de Características

| Característica | Data Warehouse | Data Lake |
| :--- | :--- | :--- |
| **Datos** | Solo estructurados (Tablas). | Estructurados, RAW, imágenes, logs, etc. |
| **Agilidad** | Menor (esquema rígido). | Mayor (esquema flexible). |
| **Usuarios** | Analistas de negocio y directivos. | Científicos de datos y desarrolladores. |
| **Costo** | Más elevado (almacenamiento premium). | Más económico (almacenamiento masivo). |
| **Calidad de datos** | Alta (datos curados y limpios). | Variable (datos en bruto). |

---

## 3. ¿Qué es un Data Mart?
Un **Data Mart** es una versión enfocada y simplificada de un Data Warehouse. Mientras que el Data Warehouse contiene datos de toda la empresa, el Data Mart se centra en un **área o departamento específico** (ej. Ventas, Marketing o Recursos Humanos).

* **Propósito:** Acelerar las consultas al reducir el volumen de datos.
* **Alcance:** Departamental.
* **Implementación:** Suele ser una "rebanada" del Data Warehouse principal.

---

## 4. Diagrama de Arquitectura de Datos

1.  **Fuentes:** CRMs, ERPs, APIs, Sensores IoT.
2.  **Ingesta:** Los datos brutos caen al **Data Lake**.
3.  **Procesamiento (ETL):** Los datos se limpian y se mueven al **Data Warehouse**.
4.  **Especialización:** Partes del Data Warehouse se dividen en **Data Marts** para cada equipo.