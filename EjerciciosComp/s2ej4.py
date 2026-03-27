empleados = [
    {"id": 1, "nombre": "Juan", "salario": 50000},
    {"id": 2, "nombre": "María", "salario": 45000},
    {"id": 3, "nombre": "Carlos", "salario": 55000}
]

print("Empleados iniciales:")
print(empleados)

# 1. Agregar un nuevo empleado
nuevo_empleado = {"id": 4, "nombre": "Ana", "salario": 47000}
empleados.append(nuevo_empleado)
print("\n1. Después de agregar nuevo empleado:")
print(empleados)

# 2. Buscar empleado por id
id_buscar = 2
empleado_encontrado = next((e for e in empleados if e["id"] == id_buscar), None)
print(f"\n2. Empleado con id={id_buscar}:", empleado_encontrado)

# 3. Calcular promedio de salarios
promedio_salario = sum(e["salario"] for e in empleados) / len(empleados)
print(f"\n3. Promedio de salarios: {promedio_salario:.2f}")

# 4. Filtrar empleados con salario > 50000
filtrados = [e for e in empleados if e["salario"] > 50000]
print("\n4. Empleados con salario > 50000:")
print(filtrados)

# 5. Actualizar el nombre del empleado con id=2
id_actualizar = 2
nuevo_nombre = "María López"
for e in empleados:
    if e["id"] == id_actualizar:
        e["nombre"] = nuevo_nombre
        break

print(f"\n5. Empleados después de actualizar nombre id={id_actualizar}:")
print(empleados)
