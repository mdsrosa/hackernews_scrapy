# -*- coding: utf-8 -*-
BOT_NAME = 'hackernews_scrapy'

SPIDER_MODULES = ['hackernews_scrapy.spiders']
NEWSPIDER_MODULE = 'hackernews_scrapy.spiders'
CONCURRENT_REQUESTS = 32
DOWNLOAD_DELAY = 5
ITEM_PIPELINES = {
    'hackernews_scrapy.pipelines.ValidateItemPipeline': 1,
    'hackernews_scrapy.pipelines.MongoDBPipeline': 2
}

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "hackernews"
MONGODB_COLLECTION = "python_articles"
