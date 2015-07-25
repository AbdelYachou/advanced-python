CREATE DATABASE DBdeCRUD;

CREATE USER 'crud'@'localhost' IDENTIFIED BY 'crom';

GRANT ALL ON DBdeCRUD.* TO 'crud'@'localhost' IDENTIFIED BY 'crom';

USE DBdeCRUD;

CREATE TABLE IF NOT EXISTS Peliculas (
   ID INT NOT NULL AUTO_INCREMENT, 
   Nombre VARCHAR(100) NOT NULL, 
   Director VARCHAR(100), 
   Genero VARCHAR(100), 
   Anio INT, 
   Descripcion VARCHAR(500), 
   PRIMARY KEY ( ID )
);
