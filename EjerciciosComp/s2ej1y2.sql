DROP TABLE IF EXISTS empleados;
DROP TABLE IF EXISTS departamentos;

CREATE TABLE departamentos (
    id INT PRIMARY KEY,
    nombre VARCHAR(100)
);

CREATE TABLE empleados (
  id INT PRIMARY KEY,
  nombre VARCHAR(100),
  departamento VARCHAR(100),
  salario INT,
  departamento_id INT,
  FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
);

INSERT INTO departamentos (id, nombre) VALUES
(1, 'IT'),
(2, 'HR'),
(3, 'Finance');

INSERT INTO empleados (id, nombre, departamento, salario, departamento_id) VALUES
(1, 'Juan', 'IT', 45000, 1),
(2, 'María', 'HR', 40000, 2),
(3, 'Carlos', 'IT', 55000, 1),
(4, 'Ana', 'Finance', 48000, 3),
(5, 'Luis', 'HR', 42000, 2);

# Consultas SQL

# Ejercicio 1
# 1. Seleccionar todos los empleados
SELECT * FROM empleados;

# 2. Seleccionar empleados del departamento IT
SELECT nombre, salario FROM empleados WHERE departamento = 'IT';

# 3. Seleccionar el empleado con el salario más alto
SELECT * FROM empleados WHERE salario = (SELECT MAX(salario) FROM empleados);

# 4. Contar el número de empleados por departamento
SELECT departamento, COUNT(*) AS total_empleados FROM empleados 
GROUP BY departamento;

# 5. Actualizar el salario de María a 50000
UPDATE empleados SET salario = 50000 WHERE nombre = 'María';


# Ejercicio 2
# 1. INNER JOIN entre empleados y departamentos
SELECT e.nombre, d.nombre AS departamento
FROM empleados e
INNER JOIN departamentos d ON e.departamento_id = d.id;

# 2. LEFT JOIN para mostrar todos los empleados y sus departamentos
SELECT e.nombre, d.nombre AS departamento
FROM empleados e
LEFT JOIN departamentos d ON e.departamento_id = d.id;

# 3. Contar empleados por departamento
SELECT e.nombre, d.nombre AS departamento
FROM empleados e
LEFT JOIN departamentos d ON e.departamento_id = d.id
GROUP BY d.nombre;