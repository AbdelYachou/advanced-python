#!/usr/python
# -*- coding: utf-8 -*-

#
# Comprobamos la consistencia de la BDdeCRUD y la reseteamos
#

import MySQLdb 

# Establecemos la conexión 
Conexion = MySQLdb.connect(host='localhost', user='crud',passwd='crom', db='DBdeCRUD') 

# Creamos el cursor 
micursor = Conexion.cursor() 

# Ahora vamos a hacer un SELECT 
query= "SELECT * FROM Peliculas WHERE 1;" 
micursor.execute(query)

# Imprimimos el numero de registros de la consulta:
print micursor.rowcount

registros= micursor.fetchall()
for registro in registros:
	print registro

# Esto que sigue es para borrar el contenido de la base de datos, 
# y que no se nos acumule al ir haciendo pruebas 
query= "DELETE FROM Peliculas WHERE 1;"
micursor.execute(query)
Conexion.commit()
# Cerramos el cursor y la conexion a la base de datos
micursor.close()
Conexion.close ()
