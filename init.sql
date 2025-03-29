-- Usar la base de datos mi_tienda
CREATE DATABASE IF NOT EXISTS mi_tienda;
USE mi_tienda;

-- Crear tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefono VARCHAR(50),
    contrasenya VARCHAR(100) NOT NULL,
    rol ENUM('cliente', 'empleado') NOT NULL DEFAULT 'cliente'
);

-- Insertar datos de ejemplo en usuarios
INSERT INTO usuarios (nombre, email, telefono, contrasenya, rol) VALUES
('Erwin', 'erwin@example.com', '635063230', 'clave123', 'cliente'),
('María', 'maria@example.com', '698745123', 'clave456', 'cliente'),
('Carlos', 'carlos@example.com', '612345678', 'clave789', 'empleado');

-- Crear tabla de joyas
CREATE TABLE IF NOT EXISTS joyas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    zona ENUM('oreja', 'nariz', 'ombligo', 'boca', 'lengua', 'ceja') NOT NULL,
    tipo ENUM('aro', 'pendiente', 'banana', 'dilatacion') NOT NULL,
    material ENUM('acero', 'oro', 'plata') NOT NULL,
    descripcion TEXT NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0
);

-- Insertar datos de ejemplo en joyas
INSERT INTO joyas (nombre, zona, tipo, material, descripcion, precio, stock) VALUES
('Aro de Acero', 'oreja', 'aro', 'acero', 'Aro pequeño de acero inoxidable', 9.99, 50),
('Pendiente de Oro', 'nariz', 'pendiente', 'oro', 'Pendiente de oro de 14K', 29.99, 20),
('Dilatador de Acrílico', 'oreja', 'dilatacion', 'acero', 'Dilatador negro de 10mm', 14.50, 30);

-- Crear tabla de citas
CREATE TABLE IF NOT EXISTS citas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    telefono VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    dni VARCHAR(40) NOT NULL,
    empleado_id INT NULL,
    fecha_hora DATETIME NOT NULL,
    estado ENUM('pendiente', 'confirmada', 'cancelada') DEFAULT 'pendiente',
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE SET NULL,
    FOREIGN KEY (empleado_id) REFERENCES usuarios(id) ON DELETE SET NULL
);

-- Insertar datos de ejemplo en citas
INSERT INTO citas (usuario_id, nombre, apellido, telefono, email, dni, empleado_id, fecha_hora, estado) VALUES
(NULL, 'Pedro', 'González', '645321789', 'pedro@example.com', '12345678X', 3, '2025-02-20 10:00:00', 'pendiente'),
(1, 'Erwin', 'Lagos', '635063230', 'erwin@example.com', '87654321Z', 3, '2025-02-21 14:30:00', 'confirmada'),
(NULL, 'Lucía', 'Martínez', '659874321', 'lucia@example.com', '34567890Y', NULL, '2025-02-22 16:00:00', 'pendiente');

-- Crear tabla de comentarios
CREATE TABLE IF NOT EXISTS comentarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    contenido TEXT NOT NULL,
    calificacion TINYINT CHECK (calificacion BETWEEN 1 AND 5),
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

-- Insertar datos de ejemplo en comentarios
INSERT INTO comentarios (usuario_id, contenido, calificacion) VALUES
(1, 'Muy buen servicio, el piercing quedó perfecto.', 5),
(2, 'Me gustó la atención, aunque tardaron un poco.', 4),
(1, 'El material de la joya es de calidad, recomendado.', 5);
