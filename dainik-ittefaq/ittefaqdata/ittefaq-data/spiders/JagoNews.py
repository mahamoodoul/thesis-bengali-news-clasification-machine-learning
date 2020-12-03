import scrapy
from ..items import ProtidindataItem
import stm as engine
import re
from bijoy2unicode import converter


class JagoNewsSpider(scrapy.Spider):
    name = 'jago'
    page_number = 339273
    source_url = 339272
    start_urls = ['https://www.dailyinqilab.com/article/339272/']

    def parse(self, response):
        items = ProtidindataItem()
        all_div_quotes = response.css('.clearfix+ .col-sm-12')
        for quote in all_div_quotes:
            lb = quote.xpath("//ol[@class='breadcrumb']//li//a/text()").extract()
            print(len(lb))
            if len(lb) >= 2:
                label = quote.xpath("//ol[@class='breadcrumb']//li//a/text()").extract()[1]
            else:
                label = None
            tit = quote.css('.col-xs-12 h1::text').extract()
            if len(tit) >= 1:
                title = quote.css('.col-xs-12 h1::text').extract()[0]
            else:
                title = None
            body = quote.css('#ar_news_content p::text').extract()
            print(len(body))
            items['label'] = label
            items['title'] = title
            items['body'] = body
            items['source'] = 'https://www.dailyinqilab.com/article/' + str(JagoNewsSpider.source_url) + '/'
            yield items
            JagoNewsSpider.source_url += 1
        next_page = 'https://www.dailyinqilab.com/article/' + str(JagoNewsSpider.page_number) + '/'
        print(next_page)
        if JagoNewsSpider.page_number < 340141:
            JagoNewsSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
