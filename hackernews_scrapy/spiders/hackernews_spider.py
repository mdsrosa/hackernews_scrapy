from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from hackernews_scrapy.items import HackernewsScrapyItem
from scrapy.selector import Selector

import datetime


class HackernewsCrawlSpider(CrawlSpider):
    name = 'pythonhackernews'
    allowed_hosts = ['news.ycombinator.com']
    start_urls = ['https://news.ycombinator.com/news?p=1']

    rules = (Rule(LinkExtractor(allow=r'news\?p=[0-9]'),
                  callback="parse_item",
                  follow=True),)

    def parse_item(self, response):
        """
            Parse the HTML to get the information we need
        """

        selector = Selector(response)
        links = selector.xpath('//td[@class="title"]')
        items = []

        for link in links:
            title = link.xpath("a/text()").extract()
            url = link.xpath("a/@href").extract()

            if title and url:
                title, url = title[0], url[0]

                item = HackernewsScrapyItem()
                item['title'] = title
                item['url'] = url
                item['crawled_at'] = datetime.datetime.utcnow()

                items.append(item)
        return items
