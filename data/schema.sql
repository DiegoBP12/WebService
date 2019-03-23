CREATE DATABASE contacts_kuorra;

USE ferreteria_DBP;

DROP TABLE IF EXISTS clientes;

CREATE TABLE IF NOT EXISTS clientes(
id_cliente INT(11) AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(50) NOT NULL COMMENT 'NOMBRE DEL CLIENTE',
apellido_paterno VARCHAR(20) NOT NULL COMMENT 'APELLIDO PATERNO DEL CLIENTE',
apellido_matero VARCHAR(20) NOT NULL COMMENT 'APELLIDO MATERNO DEL CLIENTE',
telefono VARCHAR(12) NULL COMMENT 'TELEFONO DEL CLIENTE',
email VARCHAR(50) NOT NULL COMMENT 'EMAIL DEL CLIENTE')
ENGINE = MYISAM CHARSET = LATIN1 COMMENT 'CLIENTES DE LA FERRETERIA';


INSERT INTO clientes VALUES 
(1,'Pedro','Bolanos','Castillo','7752334789','peter@quetzal.com'),
(2,'Monica Aimee','Suarez','Escorcia','7757689091','aimee@quetzal.com'),
(3,'Diego','Bolanos','Pardo','7757689342','diego@quetzal.com');

SELECT * FROM clientes;
