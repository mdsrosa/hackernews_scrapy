# HackerNews Scrapy

This is a Scrapy project to scrape the [Hacker News](https://news.ycombinator.com/) for Python articles related.

# Items

The items scraped by this project are articles, and the item is defined in the class:
```
hackernews_scrapy.items.ArticleItem
```

# Crawl Spider

This project contains a `CrawlSpider` called `pythonhackernews` that you can see by running:

`scrapy list`

## Crawl Spider: pythonhackernews

The `pythonhackernews` crawlspider scrapes the Hacker News (news.ycombinator.com) for Python articles related.

This spider doesn't crawl the entire news.ycombinator.com site but only the first 9 pages by default.

So, if you run the spider regularly (with `scrapy crawl pythonhackernews`) it will scrape only those 9 pages.

# Pipelines

This project uses two pipelines: ValidateArticlePipeline and MongoDBPipeline. 

The `ValidateArticlePipeline` can be found in this class: 
```
hackernews_scrapy.pipelines.ValidateArticlePipeline
```
This pipeline filter out websites containing 'Python' or 'python' in their title.


The `MongoDBPipeline` can be found in this class:
```
hackernews_scrapy.pipelines.MongoDBPipeline
```

This pipeline saves the articles in the MongoDB database if is not already saved.

