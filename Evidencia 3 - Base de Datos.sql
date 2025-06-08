-- Base de datos: skyroute
-- Descripción: Base de datos para gestionar clientes, destinos y ventas de una agencia de viajes.
-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS skyroute;
USE skyroute;

-- Crear tabla de clientes
CREATE TABLE clientes (
    ID_cliente INT PRIMARY KEY AUTO_INCREMENT,
    Nombre_razonsocial VARCHAR(100) NOT NULL,
    DNI_CUIT VARCHAR(20) NOT NULL,
    Correo_contacto VARCHAR(100) NOT NULL
);

-- Crear tabla de destinos
CREATE TABLE destinos (
    ID_destino INT PRIMARY KEY AUTO_INCREMENT,
    Ciudad VARCHAR(100) NOT NULL,
    Pais VARCHAR(100) NOT NULL,
    costo_base INT NOT NULL
);

-- Crear tabla de ventas
CREATE TABLE ventas (
    ID_venta INT PRIMARY KEY AUTO_INCREMENT,
    ID_cliente INT NOT NULL,
    ID_destino INT NOT NULL,
    Fecha_venta DATETIME NOT NULL,
    Costo_total INT NOT NULL,
    Estado VARCHAR(20) NOT NULL,
    Fecha_anulacion DATETIME DEFAULT NULL,
    FOREIGN KEY (ID_cliente) REFERENCES clientes(ID_cliente),
    FOREIGN KEY (ID_destino) REFERENCES destinos(ID_destino)
);

-- Insertar datos de ejemplo en clientes
INSERT INTO clientes (Nombre_razonsocial, DNI_CUIT, Correo_contacto) VALUES
('Juan Pérez', '43231560', 'juanp@gmail.com'),
('Empresa Argentina', '30-12344678-2', 'empresaArg@gmail.com'),
('María López', '87654321', 'maria.lopez@email.com');

-- Insertar datos de ejemplo en destinos
INSERT INTO destinos (Ciudad, Pais, costo_base) VALUES
('Buenos Aires', 'Argentina', 15000),
('Madrid', 'España', 35000),
('Santiago', 'Chile', 18000);

-- Insertar datos de ejemplo en ventas
INSERT INTO ventas (ID_cliente, ID_destino, Fecha_venta, Costo_total, Estado) VALUES
(1, 2, '2024-06-01 10:00:00', 35500, 'Activa'),
(2, 1, '2024-06-02 15:30:00', 15000, 'Activa'),
(3, 3, '2024-06-03 09:45:00', 18000, 'Activa');

-- Consultas útiles

-- 1. Listar todos los clientes
SELECT * FROM clientes;

-- 2. Ventas de una fecha específica
SELECT * FROM ventas WHERE DATE(Fecha_venta) = '2024-06-01';

-- 3. Última venta de cada cliente
SELECT c.Nombre_razonsocial, v.ID_venta, v.Fecha_venta
FROM clientes c
JOIN ventas v ON c.ID_cliente = v.ID_cliente
WHERE v.Fecha_venta = (
    SELECT MAX(Fecha_venta)
    FROM ventas
    WHERE ID_cliente = c.ID_cliente
);

-- 4. Destinos que empiezan con "S"
SELECT * FROM destinos WHERE Ciudad LIKE 'S%';

-- 5. Cantidad de ventas por país
SELECT d.Pais, COUNT(*) AS cantidad_ventas
FROM ventas v
JOIN destinos d ON v.ID_destino = d.ID_destino
GROUP BY d.Pais;