#!/usr/python
# -*- coding: utf-8 -*-
import MySQLdb 

def conectarBD(myHost, myUser, myPasswd, myDB):
	''' Devuelve 'Conexion' un Objecto de la clase MySQLdb.Connection 
		si la conexion se ha realiza con exito, 'None' en caso contrario.
		Keyword arguments:
			myHost   -- El host donde se aloja la BD
			myUser   -- Nombre de usuario de la BD
			myPasswd -- Contraseña de la BD
			myBD     -- Nombre de la BD
	'''
	Conexion = None
	try:
		Conexion = MySQLdb.connect(host=myHost, user=myUser,passwd=myPasswd, db=myDB) 
	except:
		print "!!Error: no se ha podido conectar a la bd: %s/%s." % (myHost, myDB)
	return Conexion

if __name__ == "__main__":

	# Establecemos la conexión a la BD
	Conexion = conectarBD('localhost', 'conan', 'crom', 'DBdeConan')
	
	if Conexion != None:

		# Creamos el cursor 
		micursor = Conexion.cursor() 
		
		# Borramos la BD
		query= "DELETE FROM Victimas WHERE 1;" 
		micursor.execute(query)
				
		# Hacemos un commit para guardar los datos
		Conexion.commit()

		# Cerramos el cursor y la conexion a la base de datos
		micursor.close()
		Conexion.close ()
	
