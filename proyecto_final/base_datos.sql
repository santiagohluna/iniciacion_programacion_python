SHOW DATABASES;

CREATE DATABASE PFI_Python;

use PFI_Python;

SHOW TABLES;

CREATE TABLE inventario(
    ID_Articulo int primary key,
    Nombre varchar(50) not null,
    Descripcion varchar(200),
    Cantidad int not null,
    Precio double not null,
    Categoria varchar(50)
);

DROP DATABASE IF EXISTS inventario;