#!/usr/python
# -*- coding: utf-8 *-*

from db_conn import DBConn

class Pelicula:

    def __init__(self, ID=None, nombre='' , director='' , genero ='', anio='', descripcion =''):
        self.nombre = nombre
        self.director = director
        self.genero = genero
        self.anio = anio
        self.descripcion = descripcion
        self.db = DBConn()
        if ID is None:
            self.ID = self.getPeliculaID()
        else:
            self.ID = ID

    def getPeliculaID(self):
        """ Obtener el ID del registro de la BD si existe """
        query = "SELECT ID FROM Peliculas WHERE Nombre = %s and Director = %s and Genero = %s and Anio = %s AND Descripcion = %s"
        values = (self.nombre, self.director, self.genero, self.anio, self.descripcion)
        resultado =  self.db.ejecutar(query, values)
        if resultado:
            return resultado[0][0]
        else:
	    return None
        
    def create(self):
        """Insertar un nuevo registro"""
        if self.ID is None:
            query = "INSERT INTO Peliculas (Nombre, Director, Genero, Anio, Descripcion) VALUES (%s, %s, %s, %s, %s)"
            values = (self.nombre, self.director, self.genero, self.anio, self.descripcion)
            self.db.ejecutar(query, values)
            # asignar un ID al objeto
            self.ID = self.getPeliculaID()
            
    def update(self):
        """Actualizar un registro existente"""
        query = "UPDATE Peliculas SET Nombre = %s, Director = %s, Genero = %s, Anio= %s, Descripcion= %s WHERE ID = %s"
        values = (self.nombre, self.director, self.genero, self.anio, self.descripcion, self.ID)
        return self.db.ejecutar(query, values)

    def read(self):
        """ Leer uno o varios registros """
        query = "SELECT * FROM Peliculas WHERE Nombre LIKE %s AND Director LIKE %s AND Genero LIKE %s AND Anio LIKE %s"
        values = ('%'+self.nombre+'%', '%'+self.director+'%', '%'+self.genero+'%', '%'+self.anio+'%')
        return self.db.ejecutar(query, values)

    def delete(self):
        """Elimina uno de los registros"""
        query = "DELETE FROM Peliculas WHERE ID = %s"
        values = self.ID
        return self.db.ejecutar(query, values)

    def read_all(self):
        """Leer todos los registros"""
        query = "SELECT * FROM Peliculas WHERE 1"
        return self.db.ejecutar(query)

