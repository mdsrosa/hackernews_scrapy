# -*- coding: utf-8 -*-
import scrapy


class ArticleItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    crawled_at = scrapy.Field(serializer=str)
