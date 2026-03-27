# Semana 2: Arquitecturas de Datos y MongoDB

## 1. Ejercicios Complementarios

[`/EjerciciosComp/`](../EjerciciosComp/)

**Ejercicios 1 y 2 (SQL):** [Ver archivo s2ej1y2.sql](../EjerciciosComp/s2ej1y2.sql) | [Ver BD s2ej1y2.db](../EjerciciosComp/s2ej1y2.db)

**Ejercicio 3 (Python):** [Ver archivo s2ej3.py](../EjerciciosComp/s2ej3.py)

**Ejercicio 4 (Python):** [Ver archivo s2ej4.py](../EjerciciosComp/s2ej4.py)

**Ejercicio 5 (Python):** [Ver archivo s2ej5.py](../EjerciciosComp/s2ej5.py)

**Ejercicio 6 (Python):** [Ver archivo s2ej6.py](../EjerciciosComp/s2ej6.py)

**Ejercicio 7 (Modelado/JSON):** [Ver archivo s2ej7.md](../EjerciciosComp/s2ej7.md)

**Ejercicio 8 (Modelado/JSON):** [Ver archivo s2ej8.md](../EjerciciosComp/s2ej8.md)

---

## 2. Actividades Prácticas

### Actividad 2.1: Investigación de Arquitecturas de Datos
[`/ActPracticas/Actividad2.1/`](../ActPracticas/Actividad2.1/)

---

**Data Warehouse vs Data Lake:** 

| Característica | Data Warehouse | Data Lake |
| :--- | :--- | :--- |
| **Datos** | Solo estructurados (Tablas). | Estructurados, RAW, imágenes, logs, etc. |
| **Agilidad** | Menor (esquema rígido). | Mayor (esquema flexible). |
| **Usuarios** | Analistas de negocio y directivos. | Científicos de datos y desarrolladores. |
| **Costo** | Más elevado (almacenamiento premium). | Más económico (almacenamiento masivo). |
| **Calidad de datos** | Alta (datos curados y limpios). | Variable (datos en bruto). |

---
**Data Mart:** Un **Data Mart** es una versión enfocada y simplificada de un Data Warehouse. Mientras que el Data Warehouse contiene datos de toda la empresa, el Data Mart se centra en un **área o departamento específico** (ej. Ventas, Marketing o Recursos Humanos).

**Diagrama:** 
1.  **Fuentes:** CRMs, ERPs, APIs, Sensores IoT.
2.  **Ingesta:** Los datos brutos caen al **Data Lake**.
3.  **Procesamiento (ETL):** Los datos se limpian y se mueven al **Data Warehouse**.
4.  **Especialización:** Partes del Data Warehouse se dividen en **Data Marts** para cada equipo.

### Actividad 2.2: Introducción a MongoDB
[`/ActPracticas/Actividad2.2/`](../ActPracticas/Actividad2.2/)
* **Base de datos:** `actividad2_2`
* **Colección:** `productos`

### Actividad 2.3: Operaciones CRUD en MongoDB
[`/ActPracticas/Actividad2.3/`](../ActPracticas/Actividad2.3/)

**Código:** 
```python
from pymongo import MongoClient

# 1. Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['actividad2_3']
empleados = db['empleados']

empleados.drop() 

#2. CREATE: Insertar documentos en la colección "empleados"
lista_empleados = [
    {"nombre": "Carlos Perez", "departamento": "Ventas", "salario": 2500},
    {"nombre": "Ana Gomez", "departamento": "Ventas", "salario": 2700},
    {"nombre": "Luis Rojas", "departamento": "IT", "salario": 3500},
    {"nombre": "Sofia Ruiz", "departamento": "IT", "salario": 3200},
    {"nombre": "Maria Leon", "departamento": "Marketing", "salario": 2200},
    {"nombre": "Jorge Diaz", "departamento": "Marketing", "salario": 2300},
    {"nombre": "Elena Sanz", "departamento": "RRHH", "salario": 2800},
    {"nombre": "Pablo Villa", "departamento": "RRHH", "salario": 2600},
    {"nombre": "Marta Soto", "departamento": "Logística", "salario": 2400},
    {"nombre": "Raul Cano", "departamento": "Logística", "salario": 2550}
]
empleados.insert_many(lista_empleados)
print("Empleados insertados correctamente.")

#3. READ: Consultar todos los documentos de "IT"
print("\nEmpleados del departamento de IT:")
for empleado in empleados.find({"departamento": "IT"}):
    print(f"Nombre: {empleado['nombre']}, Salario: {empleado['salario']}")
    
#4. UPDATE: Actualizar salario de "Carlos Perez" a 2800
empleados.update_one({"nombre": "Carlos Perez"}, {"$set": {"salario": 2800}})
print("\nSalario de Carlos Perez actualizado.")

#5. DELETE: Eliminar empleados del departamento de "Logística"
empleados.delete_many({"departamento": "Logística"})
print("\nEmpleados del departamento de Logística eliminados.")

#6. Mostrar resultados finales
print("\nEmpleados restantes en la colección:")
for empleado in empleados.find():
    print(f"Nombre: {empleado['nombre']}, Departamento: {empleado['departamento']}, Salario: {empleado['salario']}")
```

### Actividad 2.4: Modelado de Datos NoSQL
**Directorio:** [`/ActPracticas/Actividad2.4/`](../ActPracticas/Actividad2.4/)

**Justificación:** 

**Flexibilidad**
En la colección `libros`, el campo `categorias` es un Array. Lo que permite que pueda tener varias categorías al mismo tiempo de manera simple.

**Desempeño de Búsqueda**
Al usar MongoDB, podemos indexar el título y las categorías. Como los datos del libro son un solo documento, la carga de la página del libro es instantánea.

**Escalabilidad en Transacciones**
Separar los `prestamos` en una colección propia evita que el documento del `usuario` crezca demasiado con el paso de los años.

---

## 3. Actividad Evaluable: Análisis Exploratorio "Todo ventas en Línea"

### 3.1 Definición del Problema
**Objetivo del Proyecto:** Examinar el conjunto de datos de "Todo ventas en Línea, S.A. de C.V." para comprender el rendimiento de las ventas, identificar patrones y extraer información valiosa que dicte las estrategias comerciales (productos estrella, nichos de mercado y estacionalidad de promociones).

**Preguntas Clave:**
    
1.  ¿Cuáles son los productos o categorías más vendidos?
2.  ¿Existe una estacionalidad clara o picos de ventas en ciertas épocas del año?
3.  ¿Qué segmento de clientes genera los mayores ingresos?

### 3.2 Generación y Preparación de Datos
**Script de Generación:** [`generarDatos.py`](../Actividad2/generarDatos.py)

### 3.3 Análisis Exploratorio (Pandas y NumPy)
**Script de Análisis:** [`analisisEDA.py`](../Actividad2/analisisEDA.py)

**Resumen Estadístico:** [`Visualizaciones`](../Actividad2/Visualizaciones/)

[`Gráfica 1`](../Actividad2/Visualizaciones/Figure_1.png)
[`Gráfica 2`](../Actividad2/Visualizaciones/Figure_2.png)
[`Gráfica 3`](../Actividad2/Visualizaciones/Figure_3.png)
