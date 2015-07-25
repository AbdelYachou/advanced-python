#!/usr/python
# -*- coding: utf-8 *-*

import MySQLdb

class DBConn:

    def __init__(self, db_user='crud', db_pass='crom', db_host='localhost', db_name='DBdeCRUD'):
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_host = db_host
        self.db_name = db_name

    def conectar(self):
        """Crear una conexión con la base de datos"""
        self.db = MySQLdb.connect(user=self.db_user, passwd=self.db_pass, host=self.db_host, db=self.db_name)

    def abrir_cursor(self):
        """Abrir un cursor"""
        self.cursor = self.db.cursor()

    def ejecutar_consulta(self, query, values=''):
        """Ejecutar una consulta"""
        if values != '':
		    self.cursor.execute(query, values)
        else:
			self.cursor.execute(query)

    def traer_datos(self):
        """Traer todos los registros"""
        self.rows = self.cursor.fetchall()

    def enviar_commit(self, query):
        """Enviar commit a la base de datos"""
        sql = query.lower()
        es_lectura = sql.count('select')
        if es_lectura < 1:
            self.db.commit()

    def desconectar(self):
        """Cerrar cursor"""
        self.cursor.close()
        self.db.close()
        
    def ejecutar(self, query, values=''):
        """Compilar todos los procesos"""
        if (self.db_host and self.db_user and self.db_pass and self.db_name and query):
            try: 
                self.conectar()
                self.abrir_cursor()
                self.ejecutar_consulta(query, values)
                self.enviar_commit(query)
                self.traer_datos()
                self.desconectar()
            
            except MySQLdb.Error, e:
                try: 
                    print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
                except IndexError: 
                    print "MySQL Error: %s" % str(e)
            else:
		return self.rows

