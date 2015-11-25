# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log

import pymongo


class ValidateItemPipeline(object):
    def process_item(self, item, spider):
        title = item['title']
        if 'python' in title.lower():
            return item
        raise DropItem('Item is not Python related.')


class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )

        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        dict_item = dict(item)
        if not self.collection.find(dict_item):
            self.collection.insert(dict_item)
            log.msg("Article added to MongoDB database.",
                    level=log.DEBUG, spider=spider)
            return item
        raise DropItem('Item already saved to the MongoDB database.')
