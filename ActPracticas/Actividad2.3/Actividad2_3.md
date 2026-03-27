# Actividad 2.3: Operaciones CRUD en MongoDB con Python

## Script de Conexión y Operaciones CRUD
Este script realiza la conexión a la base de datos local `actividad2_3`, gestiona la colección `empleados` y ejecuta las operaciones básicas.

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

## Resultado
```bash
Empleados insertados correctamente.



Empleados del departamento de IT:

Nombre: Luis Rojas, Salario: 3500

Nombre: Sofia Ruiz, Salario: 3200



Salario de Carlos Perez actualizado.



Empleados del departamento de Logística eliminados.



Empleados restantes en la colección:

Nombre: Carlos Perez, Departamento: Ventas, Salario: 2800

Nombre: Ana Gomez, Departamento: Ventas, Salario: 2700

Nombre: Luis Rojas, Departamento: IT, Salario: 3500

Nombre: Sofia Ruiz, Departamento: IT, Salario: 3200

Nombre: Maria Leon, Departamento: Marketing, Salario: 2200

Nombre: Jorge Diaz, Departamento: Marketing, Salario: 2300

Nombre: Elena Sanz, Departamento: RRHH, Salario: 2800

Nombre: Pablo Villa, Departamento: RRHH, Salario: 2600
```