/* 
El siguiente script crea la base de datos, tablas y relaciones asociadas a estas
para el correcto funcionamiento de la aplicacion de ticket de mesa de ayuda (TMA).
*/

-- Creación del squema para la app en MySql WorkBench Developer Edition
DROP DATABASE IF EXISTS `tma`;
create schema tma;
use tma;

-- Tablas relacionadas a administración
-- area
-- criticidad
DROP TABLE IF EXISTS `criticidad`;
create table criticidad(
    id_criticidad int primary key auto_increment,
    nom_criticidad varchar(250),
    dsc_criticidad varchar(250)
);
DROP TABLE IF EXISTS `area`;
create table area(

    id_area int primary key auto_increment,
    nom_area varchar(250),
    dsc_area varchar(250)
);

-- Tablas relacionadas a usuarios
-- tipo_usuario
-- estado_usuario
-- usuario
DROP TABLE IF EXISTS `tipo_usuario`;
create table tipo_usuario(
    id_tipo_usuario int primary key auto_increment,
    nom_tipo_usuario varchar(250),
    dsc_tipo_usuario varchar(250)
);
INSERT INTO tipo_usuario (nom_tipo_usuario, dsc_tipo_usuario)
VALUES
	("root", "Acceso completo del sistema"),
	("administrador", "Usuario administrador del sistema, cuenta con acceso privilegiado al sistema"),
	("ejecutivo", "Usuario del sistema, cuenta con acceso restringido");
DROP TABLE IF EXISTS `estado_usuario`;
create table estado_usuario(
    id_estado int primary key auto_increment,
    nom_estado varchar(250),
    dsc_estado varchar(250)
);
INSERT INTO estado_usuario (nom_estado, dsc_estado)
VALUES
	("activo", "Usuario activo en el sistema"),
	("inactivo", "Usuario inactivo en el sistema");
DROP TABLE IF EXISTS `usuario`;
create table usuario(
    id_usuario int primary key auto_increment,
    nombre_usuario varchar(250),
    password varchar(250),
    id_estado int,
    id_tipo_usuario int
);
INSERT INTO usuario (nombre_usuario, password, id_estado, id_tipo_usuario)
VALUES
	("toor", "root", 1, 1),
	("aliagapato", "root", 1, 2),
	("sandrocksusana", "root", 1, 2),
	("sandrockjuan", "root", 1, 2),
	("arriagadavanessa", "root", 1, 2);
-- Tablas relacionadas a tickets
-- tipo_ticket
-- estado_ticket
-- ticket
DROP TABLE IF EXISTS `tipo_ticket`;
create table tipo_ticket(
    id_tipo_ticket int primary key auto_increment,
    nom_area varchar(250),
    dsc_tipo_ticket varchar(250)
);
DROP TABLE IF EXISTS `estado_ticket`;
create table estado_ticket(
    id_estado_ticket int primary key auto_increment,
    nom_estado_ticket varchar(250),
    dsc_estado_ticket varchar(250)
);
DROP TABLE IF EXISTS `ticket`;
create table ticket(
    id_ticket int primary key auto_increment,
    nombre_cliente varchar(20),
    rut_cliente varchar(20),
    telefono varchar(20),
    detalle varchar(500),
    observacion varchar(500),
    id_estado int,
    fecha_creacion timestamp default current_timestamp,
    id_usuario_creacion int,
    id_usuario_derivado int,
    id_criticidad int,
    id_area int,
    id_tipo_ticket int
    
);

-- Relaciones de la tabla usuario
-- usuario => usuario_tipo_usuario_fk => tipo_usuario.id_tipo_usuario
-- usuario => usuario_estado_fk => estado_usuario.id_estado
ALTER table usuario
ADD CONSTRAINT usuario_tipo_usuario_fk
FOREIGN KEY foreign_key_name(id_tipo_usuario)
REFERENCES tipo_usuario(id_tipo_usuario);
ALTER table usuario
ADD CONSTRAINT usuario_estado_fk
FOREIGN KEY foreign_key_name(id_estado)
REFERENCES estado_usuario(id_estado);

-- Relaciones de la tabla ticket
-- ticket => ticket_estado_ticket_fk => estado_ticket.id_estado_ticket
-- ticket => ticket_criticidad_fk => criticidad.id_criticidad
-- ticket => ticket_area_fk => area.id_area
-- ticket => ticket_tipo_ticket_fk => tipo_ticket.id_tipo_ticket
-- ticket => ticket_usuario_creador_fk => usuario.id_usuario
-- ticket => ticket_usuario_derivado_fk => usuario.id_usuario
ALTER table ticket
ADD CONSTRAINT ticket_estado_ticket_fk
FOREIGN KEY foreign_key_name(id_estado)
REFERENCES estado_ticket(id_estado_ticket);
ALTER table ticket
ADD CONSTRAINT ticket_criticidad_fk
FOREIGN KEY foreign_key_name(id_criticidad)
REFERENCES criticidad(id_criticidad);
ALTER table ticket
ADD CONSTRAINT ticket_area_fk
FOREIGN KEY foreign_key_name(id_area)
REFERENCES area(id_area);
ALTER table ticket
ADD CONSTRAINT ticket_tipo_ticket_fk
FOREIGN KEY foreign_key_name(id_tipo_ticket)
REFERENCES tipo_ticket(id_tipo_ticket);
ALTER table ticket
ADD CONSTRAINT ticket_usuario_creador_fk
FOREIGN KEY foreign_key_name(id_usuario_creacion)
REFERENCES usuario(id_usuario);
ALTER table ticket
ADD CONSTRAINT ticket_usuario_derivado_fk
FOREIGN KEY foreign_key_name(id_usuario_derivado)
REFERENCES usuario(id_usuario);