from scrapy.spiders import Spider
from scrapy.http import Request
from hackernews_scrapy.items import HackernewsScrapyItem
from scrapy.selector import Selector


class HackernewsSpider(Spider):
	name = 'pythonhackernews'
	allowed_hosts = ['news.ycombinator.com']
	start_urls = ['https://news.ycombinator.com']
	
	def parse(self, response):
		"""Parse the HTML to get the information we need"""
		html_xpath_selector = Selector(response)
		titles = html_xpath_selector.xpath('//td[@class="title"]/a/text()').extract()
		
		for title in titles:
			item = HackernewsScrapyItem()
			item['title'] = title
			yield item