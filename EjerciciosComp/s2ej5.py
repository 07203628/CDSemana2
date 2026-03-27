from pymongo import MongoClient

# Conectar a MongoDB local
client = MongoClient('mongodb://localhost:27017/')
db = client['tienda']
productos = db['productos']

# Limpiar colección anterior (opcional)
productos.delete_many({})

print("=== EJERCICIO 5: Operaciones CRUD en MongoDB ===\n")

# INSERTAR documentos
print("Insertando documentos...")
productos.insert_many([
    {"nombre": "Laptop", "precio": 999, "categoria": "Electrónica"},
    {"nombre": "Mouse", "precio": 29, "categoria": "Electrónica"},
    {"nombre": "Escritorio", "precio": 299, "categoria": "Muebles"}
])
print("3 documentos insertados\n")

# 1. Read: Encontrar todos los productos de Electrónica
print("Productos de Electrónica:")
electronica = list(productos.find({"categoria": "Electrónica"}))
for p in electronica:
    print(f"   - {p['nombre']}: ${p['precio']}")
print()

# 2. Read: Encontrar productos con precio < 100
print("Productos con precio < 100:")
baratos = list(productos.find({"precio": {"$lt": 100}}))
for p in baratos:
    print(f"   - {p['nombre']}: ${p['precio']}")
print()

# 3. Update: Aumentar precio de Laptop en 10%
print("Actualizando precio de Laptop (+10%)...")
productos.update_one(
    {"nombre": "Laptop"},
    {"$mul": {"precio": 1.10}}
)
laptop_actualizado = productos.find_one({"nombre": "Laptop"})
print(f"Nuevo precio: ${laptop_actualizado['precio']}\n")

# 4. Delete: Eliminar productos con precio < 50
print("Eliminando productos con precio < 50...")
resultado = productos.delete_many({"precio": {"$lt": 50}})
print(f"   - {resultado.deleted_count} producto(s) eliminado(s)\n")

# 5. Create: Agregar un nuevo producto
print("Agregando nuevo producto...")
productos.insert_one({
    "nombre": "Teclado",
    "precio": 79,
    "categoria": "Electrónica"
})
print("Teclado agregado\n")

print("=== ESTADO FINAL DE LA COLECCIÓN ===")
todos = list(productos.find())
for p in todos:
    print(f"- {p['nombre']}: ${p['precio']} ({p['categoria']})")

print(f"\nTotal de productos: {len(todos)}")

# Cerrar conexión
client.close()
