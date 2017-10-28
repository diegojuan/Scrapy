# -*- coding: utf-8 -*-
# Cargamos la libreria Scrapy
import scrapy
# Como la pagina usa JS, cargamos la libreria scrapy_splash, ya hemos
# definido la conexion en settings.py


class VinosSpider(scrapy.Spider):
    name = 'vinos'
    allowed_domains = ['dislicoresstore.com']
    start_urls = ['http://www.dislicoresstore.com/vinos.html']

    def parse(self, response):
        url_init = 'http://www.dislicoresstore.com/vinos.html'
        for i in range(1, 6):
            url = url_init + "?p=" + str(i)

            yield scrapy.Request(url, callback=self.parse_results, meta={
                'splash': {'endpoint': 'render.html',
                           'args': {'wait': 0.5}},
                'url': url
            })

    def parse_results(self, response):
        vinos = response.xpath('//*[@class="item-inner"]')
        for vino in vinos:
            nombre = vino.xpath(
                './/*[@class="product-name"]/a/@title').extract_first()
            precio = vino.xpath('.//*[@class="price"]/text()').extract_first()
            foto = vino.xpath(
                './/*[@class="primary-image"]/@src').extract_first()
            print '\n'
            print nombre
            print precio
            print foto
            print '\n'
