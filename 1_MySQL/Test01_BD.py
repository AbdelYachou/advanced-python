#!/usr/python
# -*- coding: utf-8 -*-
import MySQLdb 

# Establecemos la conexión 
Conexion = MySQLdb.connect(host='localhost', user='conan',passwd='crom', db='DBdeConan') 

# Creamos el cursor 
micursor = Conexion.cursor() 

# Ejecutamos un insert directamente 
micursor.execute("INSERT INTO Victimas (id,Nombre,Profesion,Muerte) \
	VALUES (1, \"Ejercito de Zombies\",\"Muertos Vivientes\",\"Desmembramiento a espada\");") 

# Lo mismo, pero por medio de una variable 
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) \
	VALUES (2, \"Vampiro feo\",\"Muertos Vivientes\",\"Estaca de madera\");" 
micursor.execute(query) 

query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) \
	VALUES (3, \"Bestia del Pantano\",\"Monstruo\",\"Destripado\");" 
micursor.execute(query) 

query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) \
	VALUES (4, \"Serpiente\",\"Monstruo\",\"Destripado\");" 
micursor.execute(query) 

query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) \
	VALUES (5, \"Scerdote maligno\",\"Monstruo\",\"Desmembramiento a espada\");" 
micursor.execute(query)

# Hacemos un commit, por si las moscas 
Conexion.commit()

# Ahora vamos a hacer un SELECT 
query= "SELECT * FROM Victimas WHERE 1;" 
micursor.execute(query)

# Imprimimos el numero de registros de la consulta:
print micursor.rowcount

# Obtenemos el resultado con fetchone (tambien existe fetchmany(int) fetchall)
registro= micursor.fetchone() 
print "Probando fetchone() ..."
print registro

registros= micursor.fetchmany(2)
print "Probando fetchmany(2) ..."
print registros[0]
print registros[1]

registros_resto= micursor.fetchall()
print "Probando fetchall ..."
for registro in registros:
	print registro

# Esto que sigue es para borrar el contenido de la base de datos, 
# y que no se nos acumule al ir haciendo pruebas 
query= "DELETE FROM Victimas WHERE 1;"
micursor.execute(query)

# Hacemos un commit, para guardar el borrado de datos
Conexion.commit()

# Cerramos el cursor y la conexion a la base de datos
micursor.close()
Conexion.close ()
