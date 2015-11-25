# -*- coding: utf-8 -*-
import scrapy


class HackernewsScrapyItem(scrapy.Item):
    title = scrapy.Field()
    crawled_at = scrapy.Field()
