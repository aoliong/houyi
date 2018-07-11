#!/usr/bin/python
#coding=utf8

import scrapy

from houyi.items import HouyiItem

class Spider123(scrapy.Spider):
    name = "123"
    allowed_domains = ['http://vacations.ctrip.com']
    start_urls = [
            'http://vacations.ctrip.com/tour/detail/p19489584r2001.html',
            'http://vacations.ctrip.com/tour/detail/p19494159r2001.html'
            ]

#   def parse(self, response):
#       filename = response.url.split('/')[-4]
#       with open(filename, 'wb') as f:
#           f.write(response.body)

    def parse(self, response):
        # http://vacations.ctrip.com/tour/detail/p19489584r2001.html
        # //div[@class="product_feature"]/span/p/span/text()
        for sel in response.xpath('//div[@class="product_feature"]/span/p/span/text()'):
            item = HouyiItem()
            item['body'] = sel.extract()
            print item['body']
            yield item
            # print sel.extract()

