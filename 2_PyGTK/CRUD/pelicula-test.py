#!/usr/python
# -*- coding: utf-8 -*-

#
# Probamos los distintos metodos de la clase pelicula
#

from Peliculas_Modelo import Pelicula

if __name__ == "__main__":

    peli1 = Pelicula(None, "Star Wars: Episodio IV-Una nueva esperanza", "George Lucas", "Space opera", "1977", "Conocida durante su estreno como Star Wars (o La guerra de las galaxias) es una película de 'space opera' escrita y dirigida por el director de cine estadounidense George Lucas. Fue la primera película estrenada de la serie Star Wars y la cuarta en términos de cronología interna: dos filmes subsiguientes continuarían la trama original (The Empire Strikes Back y Return of the Jedi), mientras que una trilogía (The Phantom Menace, Attack of the Clones y Revenge of the Sith)")
    peli2 = Pelicula(None, "Star Wars: Episodio V-El Imperio contraataca", "Irvin Kershner", "Space opera", "1980", "La ficción de la película se sitúa tres años después de la destrucción de la estación espacial de combate conocida como la Estrella de la Muerte.")
    peli3 = Pelicula(None, "Star Wars: Episodio VI-El retorno del jedi", "Richard Marquand", "Space opera", "1983", "Fue la tercera película estrenada de la saga de Star Wars y la sexta en términos cronológicos internos de la saga. De la trilogía original fue la película más criticada, ya que mucha gente la consideraba la más infantil por la inclusión de los ewoks.  Aún así fue aclamada por la mayoría de la gente, que la consideraron una gran, aparente, conclusión para la saga.")
    peli4 = Pelicula(None, "Star Wars: Episodio I-La amenaza fantasma", "George Lucas", "Space opera", "1999", "La peor pelicula de la saga Star Wars :(")
    peli5 = Pelicula(None, "Star Wars: Episodio II-El ataque de los clones", "George Lucas", "Space opera", "2002", "Después la Batalla de Naboo, la galaxia se encuentra al borde de una guerra civil. Bajo la dirección de un Jedi renegado que se hace llamar Conde Dooku, muchos sistemas solares amenazan con la secesión de la República Galáctica. Tras los intentos de asesinato de la senadora Padmé Amidala, la anterior reina de Naboo, el Padawan Anakin Skywalker es asignado para protegerla, mientras que a su maestro, Obi-Wan Kenobi, se le asigna la investigación del intento de asesinato.")

    # creamos los registros
    peli1.create()
    peli2.create()
    peli3.create()
    peli4.create()
    peli5.create()

    # leemos algunos registros
    print "Imprimir un registro de La DBdeCRUD.Peliculas: "
    print peli1.read()

    # actualizamos un registro
    print "Actualizamos un registro de La DBdeCRUD.Peliculas: "
    peli1.nombre = "Star Wars: Episodio IV-A new hope"
    peli1.anio = "2977"
    peli1.update()
    print "El registro id=%s de La DBdeCRUD.Peliculas fue actualizado con exito. " % peli1.ID

    # borramos un registro
    print "Borramos un registro de La DBdeCRUD.Peliculas: "
    peli4.delete()
    print "El registro id=%s de La DBdeCRUD.Peliculas fue borrado con exito. " % peli4.ID

    # leemos todos los registros
    print "Imprimir La DBdeCRUD.Peliculas: "
    pelis =  peli5.read_all()
    for peli in pelis:
        print peli
