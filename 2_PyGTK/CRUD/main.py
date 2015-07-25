#!/usr/python
# -*- coding: utf-8 -*-

try:
    import pygtk
    pygtk.require('3.0')
except:
    pass
try:
    from gi.repository import Gtk
except:
    print('GTK no encontrado')
    import sys
    sys.exit(1)

from Peliculas_Modelo import Pelicula

class Peliculas_Controlador(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self, title="Peliculas")
        self.builder = Gtk.Builder()
        self.builder.add_from_file("Peliculas_Vista.glade")

        handlers = {
            "on_window_destroy": self.on_window_destroy,
            "on_gtk_cortar_activate": self.on_gtk_cortar_activate,
            "on_gtk_copiar_activate": self.on_gtk_copiar_activate,
            "on_gtk_pegar_activate": self.on_gtk_pegar_activate,
            "on_gtk_limpiar_activate": self.on_gtk_limpiar_activate,
            "on_gtk_crear_activate": self.on_gtk_crear_activate,
            "on_gtk_consultar_activate": self.on_gtk_consultar_activate,
            "on_gtk_actualizar_activate": self.on_gtk_actualizar_activate,
            "on_gtk_borrar_activate": self.on_gtk_borrar_activate,
            "on_gtk_acerca_de_activate": self.on_gtk_acerca_de_activate,
            "on_button_clicked": self.on_button_clicked,
            "on_treeview_cursor_changed": self.on_treeview_cursor_changed
            }
        self.builder.connect_signals(handlers)

        # Model+treeView
        self.listStore = self.builder.get_object('liststore')
        self.treeView = self.builder.get_object('treeview')
        self.update_treeview()
        
        # Campos de entrada de datos
        self.datos = {}

        # Boton de ejecucion
        self.button_ejecutar = self.builder.get_object('button')

        # Barra de estado
        self.status = self.builder.get_object('statusbar')
        self.status_context_id = self.status.get_context_id('main')

        # Ventana principal
        self.window = self.builder.get_object("window")
        # Mostrar la vintana principal
        self.window.show_all()


    def on_window_destroy (self, windows):
        """ Salir de la applicacion """

        print "saliendo de la aplicacion."
        Gtk.main_quit()
    
    #
    # Menu Editar: cortar, copiar, pegar, limpiar
    # 
    def on_gtk_cortar_activate(self, *arg):

        print "cortando datos."
        self.on_gtk_copiar_activate()
        self.on_gtk_limpiar_activate()

    def on_gtk_copiar_activate(self, *arg):

        print "copiando datos."
        nombre = self.builder.get_object("entry1")
        self.datos["nombre"] = nombre.get_text()
        director = self.builder.get_object("entry2")
        self.datos["director"] = director.get_text()
        genero = self.builder.get_object("entry3")
        self.datos["genero"] = genero.get_text()
        anio = self.builder.get_object("entry4")
        self.datos["anio"] = anio.get_text()
        descripcion = self.builder.get_object("textview1")
        self.datos["descripcion"] = descripcion.get_buffer().get_text(descripcion.get_buffer().get_start_iter(),descripcion.get_buffer().get_end_iter(),True)

    def on_gtk_pegar_activate(self, *arg):

        print "pegando datos."
        if self.datos:
            nombre = self.builder.get_object("entry1")
            nombre.set_text(self.datos["nombre"])
            director = self.builder.get_object("entry2")
            director.set_text(self.datos["director"])
            genero = self.builder.get_object("entry3")
            genero.set_text(self.datos["genero"])
            anio = self.builder.get_object("entry4")
            anio.set_text(self.datos["anio"])
            descripcion = self.builder.get_object("textview1")
            descripcion.get_buffer().set_text(self.datos["descripcion"])
        else:
             self.status.push(self.status_context_id, "Error: Hay que copiar los datos antes de pegar.")

    def on_gtk_limpiar_activate(self, *arg):

        print "limpiando datos."
        nombre = self.builder.get_object("entry1")
        nombre.set_text("")
        director = self.builder.get_object("entry2")
        director.set_text("")
        genero = self.builder.get_object("entry3")
        genero.set_text("")
        anio = self.builder.get_object("entry4")
        anio.set_text("")
        descripcion = self.builder.get_object("textview1")
        descripcion.get_buffer().set_text("")
    
    #
    # Menu Pelicuals: crear, consultar, actualizar, borrar
    # 
    def on_gtk_crear_activate(self, *arg):

        print "creando registro."
        self.status.push(self.status_context_id, "Introduce los datos para crear una pelicula.")
        label_ejecutar = self.builder.get_object("label6")
        label_ejecutar.set_label("Crear pelicula:")
        self.on_gtk_limpiar_activate()
        nombre = self.builder.get_object("entry1")
        nombre.grab_focus()

    def on_gtk_consultar_activate(self, *arg):

        print "consultando registro."
        self.status.push(self.status_context_id, "Introduce los datos para consultar la/s pelicula/s.")
        label_ejecutar = self.builder.get_object("label6")
        label_ejecutar.set_label("Consultar pelicula:")
        self.on_gtk_limpiar_activate()
        nombre = self.builder.get_object("entry1")
        nombre.grab_focus()

    def on_gtk_actualizar_activate(self, *arg):

        print "actualizando registro."
        self.status.push(self.status_context_id, "Modifique los datos para actualizar una pelicula.")
        label_ejecutar = self.builder.get_object("label6")
        label_ejecutar.set_label("Actualizar pelicula:")

    def on_gtk_borrar_activate(self, *arg):

        print "borrando registro"
        self.status.push(self.status_context_id, "Seleccione una pelicula para borrar.")
        label_ejecutar = self.builder.get_object("label6")
        label_ejecutar.set_label("Borrar pelicula:")
    

    def on_button_clicked(self, *arg):
        """ Buton Ejecutar """

        print "ejecutando orden."
        
        # obtenemos los nuevos atributos de los distintos campos
        nombre = (self.builder.get_object("entry1")).get_text()
        director = (self.builder.get_object("entry2")).get_text()
        genero = (self.builder.get_object("entry3")).get_text()
        anio = (self.builder.get_object("entry4")).get_text()
        descripcion = (self.builder.get_object("textview1")).get_buffer().get_text((self.builder.get_object("textview1")).get_buffer().get_start_iter(), (self.builder.get_object("textview1")).get_buffer().get_end_iter(),True)

        # obtener la fila seleccionada: ID del objeto seleccionado
        select = self.treeView.get_selection()
        if select is not None:
            tree_model, tree_iter = select.get_selected()
        if tree_iter is not None:
	    ID = tree_model.get(tree_iter,0)[0]

        label_ejecutar = self.builder.get_object("label6")
        accion = label_ejecutar.get_label()

        if accion == "Crear pelicula:" or accion == "Consultar pelicula:":
            # creamos el objeto sin ID
            peli = Pelicula(None, nombre, director, genero, anio, descripcion)
 
            if accion == "Crear pelicula:":
                self.status.push(self.status_context_id, "Creando pelicula ...")
                resultado = peli.create()
                self.update_treeview()
                self.status.push(self.status_context_id, "Pelicula creada con exito!")
            elif accion == "Consultar pelicula:":
                self.status.push(self.status_context_id, "Consultando pelicula ...")
                resultado = peli.read()
                self.update_treeview(resultado)
                self.status.push(self.status_context_id, "Pelicula consultada con exito!")

        if accion == "Actualizar pelicula:" or accion == "Borrar pelicula:":
            # creamos el objeto con ID
            peli = Pelicula(ID,nombre, director, genero, anio, descripcion)
            if accion == "Actualizar pelicula:":
                self.status.push(self.status_context_id, "Actualizando pelicula ...")
                resultado = peli.update()
                self.update_treeview()
                self.status.push(self.status_context_id, "Pelicula actualizada con exito!")
            elif accion == "Borrar pelicula:":
                self.status.push(self.status_context_id, "Borrando pelicula ...")
                resultado = peli.delete()
                self.update_treeview()
                self.status.push(self.status_context_id, "Pelicula borrada con exito!")


    def update_treeview(self, datos=()):
        """ Metodo auxiliar para actualizar la tabla TreeView """

        self.listStore.clear()
        if not datos:
            # Crear un objeto vacio "sin ID" (para usar el metodo read_all)
            pelicula = Pelicula()
            datos = pelicula.read_all()
        if datos:
            for dato in datos:
                self.listStore.append(dato)

            self.treeView.set_cursor(0)
    

    def on_treeview_cursor_changed(self, *arg):
        """ Al pulsar en la tabla TreeView """

        select = self.treeView.get_selection()
        if select != None:
            tree_model, tree_iter = select.get_selected()
            if tree_model != None and tree_iter != None:
                nombre = self.builder.get_object("entry1")
                nombre.set_text(tree_model.get(tree_iter,1)[0])
                director = self.builder.get_object("entry2")
                director.set_text(tree_model.get(tree_iter,2)[0])
                genero = self.builder.get_object("entry3")
                genero.set_text(tree_model.get(tree_iter,3)[0])
                anio = self.builder.get_object("entry4")
                anio.set_text(str(tree_model.get(tree_iter,4)[0]))
                descripcion = self.builder.get_object("textview1")
                descripcion.get_buffer().set_text(tree_model.get(tree_iter,5)[0])

    #
    # Ventana acerca de
    #
    def on_gtk_acerca_de_activate(self, *arg):

        print "ayuda acerca de seleccionado."
        self.aboutdialog = self.builder.get_object("aboutdialog")
        self.aboutdialog.run()
        self.aboutdialog.hide()


if __name__ == "__main__":
    win = Peliculas_Controlador()
    Gtk.main()


