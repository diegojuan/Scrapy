# -*- coding: utf-8 -*-
# Cargamos la libreria Scrapy
import scrapy


class VinosSpider(scrapy.Spider):
    name = 'vinos'
    allowed_domains = ['dislicoresstore.com']
    start_urls = ['http://www.dislicoresstore.com/vinos.html']

    def parse(self, response):

        for i in range(1, 6):
            url = VinosSpider.start_urls[0] + "?p=" + str(i)

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

            print(nombre.strip() + ': ' + precio.strip() + '\n')
