# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class VinosSpider(scrapy.Spider):
    name = 'vinos'
    allowed_domains = ['www.dislicores.com']
    start_urls = ['http://www.dislicores.com/vinos.html']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        pass
