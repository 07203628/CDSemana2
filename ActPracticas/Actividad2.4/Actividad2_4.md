# Actividad 2.4: Modelado de Datos NoSQL

## 1. Diseño de Colecciones y estructura
En este modelo, utilizaremos una combinación de referencias (para datos que crecen mucho) e información embebida (para optimizar las consultas de lectura).

**1.1. Colección: `libros`**
Es la colección principal. Almacena metadatos del libro y una referencia a los autores.
```json
{
  "_id": "ObjectId",
  "titulo": "String",
  "isbn": "String",
  "autores": ["ObjectId"], 
  "categorias": ["String"],
  "anio_publicacion": "Int",
  "editorial": "String",
  "copias_disponibles": "Int",
  "idioma": "String"
}
```

**1.2. Colección: `autores`**
Información detallada sobre los autores.
```json
{
  "_id": "ObjectId",
  "nombre": "String",
  "biografia": "String",
  "nacionalidad": "String",
  "fecha_nacimiento": "Date"
}
```

**1.3. Colección: `usuarios`**
Datos de los usuarios y su estado de suscripción.
```json
{
  "_id": "ObjectId",
  "nombre": "String",
  "biografia": "String",
  "nacionalidad": "String",
  "fecha_nacimiento": "Date"
}
```

**1.4. Colección: `prestamos`**
Registra la transacción de entrada y salida de los libros.
```json
{
  "_id": "ObjectId",
  "libro_id": "ObjectId",
  "usuario_id": "ObjectId",
  "fecha_salida": "Date",
  "fecha_devolucion_esperada": "Date",
  "fecha_devolucion_real": "Date",
  "estado": "String" // Ejemplo: 'Activo', 'Devuelto', 'Atrasado'
}
```

**1.5 Colección: `reviews`**
Opiniones de los usuarios sobre los libros.
```json
{
  "_id": "ObjectId",
  "libro_id": "ObjectId",
  "usuario_id": "ObjectId",
  "calificacion": "Int", // Escala 1-5
  "comentario": "String",
  "fecha_publicacion": "Date"
}
```

# 2. Justificación del diseño 

**2.1 Flexibilidad**
En la colección `libros`, el campo `categorias` es un Array. Lo que permite que pueda tener varias categorías al mismo tiempo de manera simple.

**2.2 Desempeño de Búsqueda**
Al usar MongoDB, podemos indexar el título y las categorías. Como los datos del libro son un solo documento, la carga de la página del libro es instantánea.

**2.3 Escalabilidad en Transacciones**
Separar los `prestamos` en una colección propia evita que el documento del `usuario` crezca demasiado con el paso de los años.
