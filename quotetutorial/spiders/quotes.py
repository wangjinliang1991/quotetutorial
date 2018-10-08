# -*- coding: utf-8 -*-
import scrapy

from ..items import QuoteItem



class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('.quote')
        for quote in quotes:
            # 对于text节点，获取正文内容，加::text获取，结果为长度为1的列表，获取第一个元素
            item = QuoteItem()
            text = quote.css('.text::text').extract_first()
            author = quote.css('.author::text').extract_first()
            tags = quote.css('.tags .tag::text').extract()
            item['text'] = text
            item['author'] = author
            item['tags'] = tags
            yield item

        next = response.css('.pager .next a::attr(href)').extract_first()
        url = response.urljoin(next)
        # callback回调函数，请求完成后获得响应，引擎将该响应作为参数传递给回调函数，进行解析或生成下一个请求
        yield scrapy.Request(url=url, callback=self.parse)
