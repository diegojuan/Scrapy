# -*- coding: utf-8 -*-
# Cargamos la libreria Scrapy
import scrapy
# Como la pagina usa JS, cargamos la libreria scrapy_splash, ya hemos
# definido la conexion en settings.py

from scrapy_splash import SplashRequest


class VinosSpider(scrapy.Spider):
    name = 'vinos'
    allowed_domains = ['dislicoresstore.com']
    start_urls = ['http://www.dislicoresstore.com/vinos.html']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                                endpoint='render.html',
                                args={'wait': 0.5},
                                )

    def parse(self, response):

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

        #next_page_url = response.xpath('//*[@class="button next i-next"]/@href').extract_first()
        #next_page_url = "http://www.dislicoresstore.com/vinos.html?p=4"
        for i in range(2, 5):
            next_page_url = "http://www.dislicoresstore.com/vinos.html?p=" + \
                str(i)
        #   print next_page_url
            yield scrapy.Request(next_page_url)
