# -*- coding: utf-8 -*-


BOT_NAME = 'scrapy_osl'

SPIDER_MODULES = ['scrapy_osl.spiders']
NEWSPIDER_MODULE = 'scrapy_osl.spiders'

ITEM_PIPELINES = {
    'scrapy_osl.pipelines.PipelineConEtiqueta' : 1, 
    'scrapy_osl.pipelines.PipelineSinEtiqueta' : 2
    }
