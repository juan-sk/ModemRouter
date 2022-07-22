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

INSERT INTO
    criticidad (id_criticidad, nom_criticidad, dsc_criticidad)
VALUES
    (
        1,
        "Baja",
        "El sistema puede funcionar sin impactar la operación"
    ),
    (
        2,
        "Media",
        "La operación del sistema se ve impacatada"
    ),
    (
        3, 
        "Alta", 
        "El sistema no puede operar"
    );

DROP TABLE IF EXISTS `area`;

create table area(
    id_area int primary key auto_increment,
    nom_area varchar(250),
    dsc_area varchar(250)
);

INSERT INTO
    area (id_area, nom_area, dsc_area)
VALUES
    (
        1,
        "Marketing",
        "Área encargada de la publicidad y relaciones publicas de la empresa"
    ),
    (
        2,
        "TI",
        "Área encarga del soporte informatico interno"
    ),
    (
        3,
        "Finanzas",
        "Área encargada de la contabilidad de la empresa}"
    ),
    (
        4,
        "Recursos humanos",
        "Área encargada de adminsitrar el capital humano de la empresa"
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

INSERT INTO
    tipo_usuario (
        id_tipo_usuario,
        nom_tipo_usuario,
        dsc_tipo_usuario
    )
VALUES
    (
        1,
        "Jefe de mesa",
        "Usuario administrador del sistema, cuenta con acceso privilegiado al sistema"
    ),
    (
        2,
        "Ejecutivo de mesa",
        "Usuario del sistema, cuenta con acceso restringido, puede generar tickets"
    ),
    (
        3,
        "Ejecutivo espefico",
        "Usuario del sistema, cuenta con acceso restringido, puede gestionar ticket"
    );

DROP TABLE IF EXISTS `estado_usuario`;

create table estado_usuario(
    id_estado int primary key auto_increment,
    nom_estado varchar(250),
    dsc_estado varchar(250)
);

INSERT INTO
    estado_usuario (id_estado, nom_estado, dsc_estado)
VALUES
    (1, "activo", "Usuario activo en el sistema"),
    (2, "inactivo", "Usuario inactivo en el sistema");

DROP TABLE IF EXISTS `usuario`;

create table usuario(
    id_usuario int primary key auto_increment,
    nombre_usuario varchar(250),
    password varchar(250),
    id_estado int,
    id_tipo_usuario int
);

-- Tipos de usuario 1, 2, 3
-- Jefe de mesa
-- Ejecutivo de mesa
-- Ejecutivo espefico
INSERT INTO
    usuario (
        nombre_usuario,
        password,
        id_estado,
        id_tipo_usuario
    )
VALUES
    ("jefe", "jefe", 1, 1),
    ("mesa1", "mesa1", 1, 2),
    ("mesa2", "mesa2", 1, 2),
    ("spec1", "spec1", 1, 3),
    ("spec2", "spec2", 1, 3);

DROP TABLE IF EXISTS `area_usuario`;

create table area_usuario(
    id_usuario int,
    id_area int
);

INSERT INTO
    area_usuario (
        id_usuario,
        id_area
    )
VALUES
    (4, 1),
    (5, 1),
    (4, 2),
    (5, 3),
    (4, 4),
    (5, 4);

-- Tablas relacionadas a tickets
-- tipo_ticket
-- estado_ticket
-- ticket
DROP TABLE IF EXISTS `tipo_ticket`;

create table tipo_ticket(
    id_tipo_ticket int primary key auto_increment,
    nom_tipo_ticket varchar(250),
    dsc_tipo_ticket varchar(250)
);

INSERT INTO
    tipo_ticket(id_tipo_ticket, nom_tipo_ticket, dsc_tipo_ticket)
VALUES
    (
        1,
        "Felicitación",
        "Se desea felicitar a algun funcionario o proceso de la empresa"
    ),
    (
        2,
        "Consulta",
        "Se desea consultar alguna información en particular"
    ),
    (
        3,
        "Reclamo",
        "Se desea reclamar por algun funcionario o proceso de la empresa"
    ),
    (
        4,
        "Problema",
        "Se desea reportar un problema de funcionamiento"
    );

DROP TABLE IF EXISTS `estado_ticket`;

create table estado_ticket(
    id_estado_ticket int primary key auto_increment,
    nom_estado_ticket varchar(250),
    dsc_estado_ticket varchar(250)
);

INSERT INTO estado_ticket(nom_estado_ticket, dsc_estado_ticket)
VALUES 
    ('Abierto', 'Ticket en trabajo'),
    ('Cerrado', 'Ticket finalizado');

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
    id_tipo_ticket int,
    correo_electronico varchar(250)
);

INSERT INTO ticket (
  nombre_cliente,
  rut_cliente,
  telefono,
  detalle,
  observacion,
  id_estado,
  fecha_creacion,
  id_usuario_creacion,
  id_usuario_derivado,
  id_criticidad,
  id_area,
  id_tipo_ticket,
  correo_electronico
) VALUES 
  ('Coca Cola', '11222333-4', '987654321', 'Se quiere feliciar a S.Sandrock por su excelente disposición',  '',  1,  current_timestamp,  2,  4,  3,  4,  1, 'contacto@cocacola.cl'),
  ('Coca Cola', '11222333-4', '987654321', 'Actor equivocado en el spot de marzo 2022',  '',  1,  current_timestamp,  3,  5,  3,  1,  3, 'contacto@cocacola.cl'),
  ('Coca Cola', '11222333-4', '987654321', 'Maquina de mall plaza tobalaba sin funcionar',  '',  1,  current_timestamp,  2,  4,  3,  2,  2, 'contacto@cocacola.cl'),
  ('Coca Cola', '11222333-4', '987654321', 'Maquina de mall del centro sin funcionar',  '',  1,  current_timestamp,  3,  5,  3,  2,  2, 'contacto@cocacola.cl'),
  ('Pepsi', '99888777-2', '9752371253', 'Se quiere feliciar a J.Sandrock por su excelente disposición',  '',  1,  current_timestamp,  2,  4,  3,  4,  1, 'contacto@pepsi.cl'),
  ('Pepsi', '99888777-2', '9752371253', 'Despacho de prodcutos no entregado en sucursal correcta',  '',  1,  current_timestamp,  3,  5,  3,  1,  3, 'contacto@pepsi.cl'),
  ('Pepsi', '99888777-2', '9752371253', 'Maquina gasificadora de la fuente alemana no funciona',  '',  1,  current_timestamp,  2,  4,  3,  2,  2, 'contacto@pepsi.cl'),
  ('Pepsi', '99888777-2', '9752371253', 'Mantención de maquinas del estadio nacional',  '',  1,  current_timestamp,  3,  5,  3,  2,  2, 'contacto@pepsi.cl');

-- Relaciones de la tabla usuario
-- usuario => usuario_tipo_usuario_fk => tipo_usuario.id_tipo_usuario
-- usuario => usuario_estado_fk => estado_usuario.id_estado
ALTER table
    usuario
ADD
    CONSTRAINT usuario_tipo_usuario_fk FOREIGN KEY foreign_key_name(id_tipo_usuario) REFERENCES tipo_usuario(id_tipo_usuario);

ALTER table
    usuario
ADD
    CONSTRAINT usuario_estado_fk FOREIGN KEY foreign_key_name(id_estado) REFERENCES estado_usuario(id_estado);

-- Relaciones de la tabla ticket
-- ticket => ticket_estado_ticket_fk => estado_ticket.id_estado_ticket
-- ticket => ticket_criticidad_fk => criticidad.id_criticidad
-- ticket => ticket_area_fk => area.id_area
-- ticket => ticket_tipo_ticket_fk => tipo_ticket.id_tipo_ticket
-- ticket => ticket_usuario_creador_fk => usuario.id_usuario
-- ticket => ticket_usuario_derivado_fk => usuario.id_usuario
ALTER table
    ticket
ADD
    CONSTRAINT ticket_estado_ticket_fk FOREIGN KEY foreign_key_name(id_estado) REFERENCES estado_ticket(id_estado_ticket);

ALTER table
    ticket
ADD
    CONSTRAINT ticket_criticidad_fk FOREIGN KEY foreign_key_name(id_criticidad) REFERENCES criticidad(id_criticidad);

ALTER table
    ticket
ADD
    CONSTRAINT ticket_area_fk FOREIGN KEY foreign_key_name(id_area) REFERENCES area(id_area);

ALTER table
    ticket
ADD
    CONSTRAINT ticket_tipo_ticket_fk FOREIGN KEY foreign_key_name(id_tipo_ticket) REFERENCES tipo_ticket(id_tipo_ticket);

ALTER table
    ticket
ADD
    CONSTRAINT ticket_usuario_creador_fk FOREIGN KEY foreign_key_name(id_usuario_creacion) REFERENCES usuario(id_usuario);

ALTER table
    ticket
ADD
    CONSTRAINT ticket_usuario_derivado_fk FOREIGN KEY foreign_key_name(id_usuario_derivado) REFERENCES usuario(id_usuario);