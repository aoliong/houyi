#!/usr/bin/python
#coding=utf8

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from houyi.items import HouyiItem

import logging
from scrapy.utils.log import configure_logging


class Spider123(CrawlSpider):
    name = "ctrip"
    allowed_domains = ['vacations.ctrip.com', 'baidu.com']
    start_urls = [
            'http://weekend.ctrip.com/around/guangzhou-dest/taocan/?keyword=%E5%B9%BF%E4%B8%9C#ctm_ref=gs-100000792-290801-32-02-G001|04|guangdong',
            ]

    rules = (
            Rule(LinkExtractor(), callback='parse_item'),
    )

    def parse_start_url(self, response):
        # self.logger.info('start url')
        # 找出所有景点的URL
        count = 0
        for sel in response.xpath('//div[@class="product_m"]/h2/a/@href'):
            if count == 0:
                url = sel.extract()
                item = HouyiItem()
                item['body'] = url
                r = self.make_requests_from_url(url)
                self.logger.info('url:%s' % url)
            count += 1

        # 找出所有URL
#       for sel in response.xpath('//a/@href'):
#           yield sel.extract()

        # 找出所下页数的URL
#       for sel in response.xpath('//div[@class="pkg_page basefix"]/a/@href'):
#           self.logger.info('lyx! %s' % sel.extract())
#           yield sel.extract()


    def parse_item(self, response):
        # http://vacations.ctrip.com/tour/detail/p19489584r2001.html
        # //div[@class="product_feature"]/span/p/span/text()
        # 获取其它景点的链接
        # //div[@class="product_m"]/h2/a/@href

        self.logger.info('url:%s' % response.url)
        return None
        # self.logger.info('text : %s' % response.xpath('//div[@class="product_feature"]/span/p/span/text()'))

#       for sel in response.xpath('//div[@class="product_feature"]/p/span/text()'):
#           item = HouyiItem()
#           body = sel.extract()
#           item['body'] = body
#           # self.logger.info('body is: %s' % item['body'])
#           yield item
#           # print sel.extract()



