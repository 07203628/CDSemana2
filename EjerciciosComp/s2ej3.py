import json

datos = {
  "empleados": [
    {"id": 1, "nombre": "Juan", "habilidades": ["Python", "SQL"]},
    {"id": 2, "nombre": "María", "habilidades": ["Java", "MongoDB"]},
    {"id": 3, "nombre": "Carlos", "habilidades": ["Python", "R"]}
  ]
}

# 1. Extraer los nombres de todos los empleados
nombres = [e["nombre"] for e in datos["empleados"]]
print("1. Nombres de empleados:", nombres)

# 2. Agregar una nueva habilidad a Juan
for e in datos["empleados"]:
    if e["nombre"] == "Juan":
        e["habilidades"].append("JavaScript")
        print("2. Habilidades de Juan tras agregar JavaScript:", e["habilidades"])
        break

# 3. Crear un nuevo empleado con id: 4
nuevo_empleado = {"id": 4, "nombre": "Laura", "habilidades": ["Docker", "Git"]}
datos["empleados"].append(nuevo_empleado)
print("3. Nuevo empleado agregado:", nuevo_empleado)

# 4. Eliminar las habilidades de María
for e in datos["empleados"]:
    if e["nombre"] == "María":
        e["habilidades"] = []
        print("4. Habilidades de María eliminadas, ahora:", e["habilidades"])
        break

print("\nJSON final:")
print(json.dumps(datos, indent=2, ensure_ascii=False))
