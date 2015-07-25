# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request

from scrapy_osl.items import OSLItem

class oslSpider(Spider):

    name = 'scrapy_osl'
    allowed_domains = ['osl.ugr.es']
    start_urls = ['http://osl.ugr.es/']

    def parse(self, response):
        items =[]
        # Instancia un selector
        hxs = Selector(response)

        # Selecciona los posts de la página principal
        url_posts = hxs.xpath("//h2[contains(@class,'entry')]/a/@href").extract()

        # Recorre los posts extrayendo la información
        for url_post in url_posts:
            yield Request(url_post, callback=self.parse_posts)
            
    def parse_posts(self, response):
		
        sel = Selector(response)
        item = OSLItem()
        
        item['titulo'] = sel.xpath("//header/h1[contains(@class,'entry-title')]/text()").extract()
        item['autor'] = sel.xpath("//header/div[@class='entry-meta']/span[@class='by-author']/span[@class='author vcard']/a/text()").extract()
        item['contenido'] = sel.xpath("//section/p/text()").extract()
        item['categorias'] = sel.xpath("//header/div[@class='entry-meta']/a[@class='btn btn-mini']/text()").extract()
        item['etiquetas'] = sel.xpath("//header/div[@class='entry-meta']/a[@class='btn btn-mini btn-tag']/text()").extract()

        return item
