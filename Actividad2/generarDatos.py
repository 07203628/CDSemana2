import random
from datetime import datetime, timedelta
from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


client = MongoClient('mongodb://localhost:27017/')
db = client['actividad_semana2']
coleccion_ventas = db['ventas'] 

# Limpiar colección previa
coleccion_ventas.drop()

productos = [
    {"nombre": "Iphone 15", "categoria": "Telefonos", "precio": 760.00},
    {"nombre": "Samsung Galaxy S23", "categoria": "Telefonos", "precio": 699.99},
    {"nombre": "MacBook Pro", "categoria": "Tecnología", "precio": 1299.99},
    {"nombre": "iPad Air", "categoria": "Tecnología", "precio": 599.99},
    {"nombre": "AirPods Pro", "categoria": "Accesorios", "precio": 249.99}
]

ciudades = ["Phoenix", "Dallas", "San Antonio", "San Diego", "San Jose"]
generos = ["Masculino", "Femenino", "Otro"]

ventas_simuladas = []
fecha_inicio = datetime(2026, 1, 1)

for _ in range(1000):
    producto = random.choice(productos)
    cantidad = random.randint(1, 3)
    
    fecha_random = random.randint(0, 365)
    if random.random() > 0.7: 
        fecha_random = random.randint(300, 365)
        
    fecha_venta = fecha_inicio + timedelta(days=fecha_random)
        
    venta = {
        "producto": producto["nombre"],
        "categoria": producto["categoria"],
        "precio_unitario": producto["precio"],
        "cantidad": cantidad,
        "fecha_venta": fecha_venta,
        "total_venta": round(producto["precio"] * cantidad, 2),
        "cliente": {
            "edad": random.randint(18, 65),
            "genero": random.choices(generos, weights=[0.5, 0.4, 0.1])[0],
            "ciudad": random.choices(ciudades, weights=[0.3, 0.25, 0.2, 0.15, 0.15])[0]
        }
    }
    ventas_simuladas.append(venta)
    
coleccion_ventas.insert_many(ventas_simuladas)
print("Datos simulados insertados en MongoDB.")