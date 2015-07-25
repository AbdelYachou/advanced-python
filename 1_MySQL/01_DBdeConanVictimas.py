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

def insertar(ID, Nombre, Profesion, Muerte, cursorBD):
	''' Inserta un registro en la tabla DBdeConan.Victimas.
		Keyword arguments:
			ID        -- identificador del registro
			Nombre    -- valor del campo Victimas.Nombre
			Profesion -- valor del campo Victimas.Profesion
			Muerte    -- valor del campo Victimas.Muerte
	'''
	query= ("INSERT INTO Victimas " 
			"(id,Nombre,Profesion,Muerte) " 
			"VALUES (%s, %s, %s, %s)")
	data = (ID, Nombre, Profesion, Muerte)
	cursorBD.execute(query, data)


if __name__ == "__main__":

	# Establecemos la conexión a la BD
	Conexion = conectarBD('localhost', 'conan', 'crom', 'DBdeConan')
	
	if Conexion != None:

		# Creamos el cursor 
		micursor = Conexion.cursor() 
		
		# Insertamos 10 registros  
		insertar(1, "Ejercito de Zombies","Muertos Vivientes","Desmembramiento a espada", micursor)
		insertar(2, "Vampiro feo","Muertos Vivientes","Estaca de madera", micursor)
		insertar(3, "Bestia del Pantano","Monstruo","Destripado", micursor)
		insertar(4, "Serpiente","Monstruo","Destripado", micursor)
		insertar(5, "Scerdote maligno","Monstruo","Desmembramiento a espada", micursor)
		insertar(6, "Ejercito de Zombies 2","Muertos Vivientes","Desmembramiento a espada", micursor)
		insertar(7, "Vampiro feo 2","Muertos Vivientes","Estaca de madera", micursor)
		insertar(8, "Bestia del Pantano 2","Monstruo","Destripado", micursor)
		insertar(9, "Serpiente 2","Monstruo","Destripado", micursor)
		insertar(10, "Scerdote maligno 2","Monstruo","Desmembramiento a espada", micursor)
		
		# Guardamos el ultimo id de la BD
		i =10
		
		while(raw_input("¿Desea añadir un nuevo registro a la BD s/n? ") in ['s', 'S', 'si', 'Si', 'SI']):
			
			nombre = raw_input("\tIntroduce el nombre: ")
			profesion = raw_input("\tIntroduce la profesion: ")
			muerte = raw_input("\tIntroduce la muerte: ")
			
			if (nombre == '' or profesion == '' or muerte == ''):
				print "!!Warning: Registro no insertado, no se admiten campos vacios en la BD.\n"
				continue
			else:
				i += 1
				insertar(i, nombre, profesion, muerte, micursor)
				print "!!Info: Registro insertado con exito.\n"
				
		# Hacemos un commit para guardar los datos
		Conexion.commit()

		# Ahora vamos a mostrar los registros 
		query= "SELECT * FROM Victimas WHERE 1;" 
		micursor.execute(query)

		# Obtenemos el resultado con fetchall
		registros = micursor.fetchall()
		print "Imprimiendo la base de datos Victimas ..."
		for registro in registros:
			print registro

		# Cerramos el cursor y la conexion a la base de datos
		micursor.close()
		Conexion.close ()
