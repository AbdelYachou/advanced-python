# -*- coding: utf-8 -*-

from scrapy import Item
from scrapy.item import Field


class OSLItem(Item):

    titulo = Field()
    autor = Field()
    contenido = Field()
    categorias = Field()
    etiquetas = Field()
