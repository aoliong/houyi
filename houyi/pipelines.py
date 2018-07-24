# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json, os

class HouyiPipeline(object):
    def __init__(self):
        self.filename = 'data_cn'
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def process_item(self, item, spider):
        print '****item: %s' % item
        data = json.dumps(dict(item)) + '\n'
        with codecs.open(self.filename, 'a', encoding='utf-8') as f:
            f.write(data.decode('unicode_escape'))
        return item
