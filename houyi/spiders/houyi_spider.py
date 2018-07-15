#!/usr/bin/python
#coding=utf8

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from houyi.items import HouyiItem

class Spider123(CrawlSpider):
    name = "ctrip"
    allowed_domains = ['vacations.ctrip.com']
    start_urls = [
            'http://weekend.ctrip.com/around/guangzhou-dest/taocan/?keyword=%E5%B9%BF%E4%B8%9C#ctm_ref=gs-100000792-290801-32-02-G001|04|guangdong',
            ]

    rules = (
            Rule(LinkExtractor(), callback='parse_item'),
    )

    def parse_item(self, response):
        # http://vacations.ctrip.com/tour/detail/p19489584r2001.html
        # //div[@class="product_feature"]/span/p/span/text()
        # 获取其它景点的链接
        # //div[@class="product_m"]/h2/a/@href

        self.logger.info('****hello')
        self.logger.info('Hi, this is an item page! %s' % response.url)

        for sel in response.xpath('//div[@class="product_feature"]/span/p/span/text()'):
            item = HouyiItem()
            item['body'] = sel.extract()
            self.logger.info('body is: %s' % item['body'])
            yield item
            # print sel.extract()



