import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['escuela']
nombre = db['nombre']

nombre.delete_many({})

print("=== EJERCICIO 6: Operaciones CRUD en MongoDB ===\n")

print("Insertando documentos...")
nombre.insert_many([
    {"nombre": "Ana", "materias": ["Math", "Physics"], "edad": 20},
    {"nombre": "Luis", "materias": ["Math", "Chemistry"], "edad": 22},
    {"nombre": "Sofia", "materias": ["Biology"], "edad": 19}
])

# 1. Read: Encontrar estudiantes con Math
print("Encontrar estudiantes con Math")
estudiantes_math = list(nombre.find({"materias": "Math"}))
for e in estudiantes_math:
    print(f"   - {e['nombre']}, edad: {e['edad']}")
print()

# 2. Read: Encontrar estudiantes mayores de 20 años
print("Encontrar estudiantes mayores de 20 años")
estudiantes_mayores = list(nombre.find({"edad": {"$gt": 20}}))
for e in estudiantes_mayores:
    print(f"   - {e['nombre']}, edad: {e['edad']}")
print()

# 3. Contar estudiantes por edad
print("Contar estudiantes por edad")
conteo_edad = nombre.aggregate([
    {"$group": {"_id": "$edad", "count": {"$sum": 1}}}
])
for c in conteo_edad:
    print(f"   - Edad: {c['_id']}, Cantidad: {c['count']}")
print()

# 4. Proyectar solo nombres
print("Proyectar solo nombres")
nombres = list(nombre.find({}, {"_id": 0, "nombre": 1}))
for n in nombres:
    print(f"   - {n['nombre']}")
print()    