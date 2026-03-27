import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['actividad_semana2']
datos = list(db['ventas'].find({}, {"_id": 0}))

df = pd.json_normalize(datos)
df['fecha_venta'] = pd.to_datetime(df['fecha_venta'])
df.head()

plt.figure(figsize=(10, 6))
ventas_por_producto = df.groupby('producto')['total_venta'].sum().sort_values(ascending=False)

sns.barplot(x=ventas_por_producto.values, y=ventas_por_producto.index, palette='viridis')
plt.title('Ventas Totales por Producto')
plt.xlabel('Ventas Totales')
plt.ylabel('Producto')
plt.show()

fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Distribución de edades de los clientes
sns.histplot(df['cliente.edad'], bins=20, kde=True, ax=axes[0], color='skyblue')
axes[0].set_title('Distribución de Edades de los Clientes')
axes[0].set_xlabel('Edad')

# Distribución de clientes por ciudad
sns.countplot(x='cliente.ciudad', data=df, ax=axes[1], palette='Set2')
axes[1].set_title('Distribución de Clientes por Ciudad')
axes[1].set_xlabel('Ciudad')
axes[1].set_ylabel('Cantidad de Clientes')

# Mostrar las gráficas
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
df['mes_venta'] = df['fecha_venta'].dt.to_period('M')
ventas_por_mes = df.groupby('mes_venta')['total_venta'].sum()

sns.lineplot(x=ventas_por_mes.index.astype(str), y=ventas_por_mes.values, marker='o', color='coral')
plt.title('Tendencia de Ventas Mensuales')
plt.xlabel('Mes de Venta')
plt.ylabel('Ingresos Totales')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()