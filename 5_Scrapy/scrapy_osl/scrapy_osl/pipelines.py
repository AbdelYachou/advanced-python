# -*- coding: utf-8 -*-

from scrapy import signals
from scrapy.exporters import XmlItemExporter
from scrapy.xlib.pydispatch import dispatcher
import logging

class Pipeline(object):
	
    def __init__(self):
        self.files = {}
        
        # Conexión de las señales de apertura y cierre del spider
        dispatcher.connect(self.spider_opened, signals.spider_opened)
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()
        

class PipelineConEtiqueta(Pipeline):

    def spider_opened(self, spider):
        file = open('%s_con_etiquetas.xml' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = XmlItemExporter(file)
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        # Al menos una etiqueta definida, exporta el item
        if item['etiquetas']:
            logging.log(logging.INFO, 'Procesando el elemento con etiqueta: %s' % item['titulo'])
            self.exporter.export_item(item)

        return item
    
    
class PipelineSinEtiqueta(Pipeline):

    def spider_opened(self, spider):
        file = open('%s_sin_etiquetas.xml' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = XmlItemExporter(file)
        self.exporter.start_exporting()


    def process_item(self, item, spider):
        # Al menos una etiqueta definida, exporta el item
        if not item['etiquetas']:
            logging.log(logging.INFO, 'Procesando el elemento sin etiqueta: %s' % item['titulo'])
            self.exporter.export_item(item)

        return item
