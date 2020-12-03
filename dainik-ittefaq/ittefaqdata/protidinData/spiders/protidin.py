import scrapy
from ..items import ProtidindataItem
import stm as engine
import re
from bijoy2unicode import converter


class ProtidinSpider(scrapy.Spider):
    name = 'protidin'
    page_number = 836
    start_urls = ['https://www.dailyinqilab.com/newscategory/sports/?page=835']

    def parse(self, response):
        items = ProtidindataItem()
        all_div_quotes = response.css('div.col-sm-6')
        count = 1
        for quote in all_div_quotes:
            label = 'sports'
            title = quote.css('h2::text').extract()[0]
            # n1 = self.cleanData(title)
            # test = converter.Unicode()
            # toPrint = test.convertBijoyToUnicode(n1)
            # print(toPrint)
            body = quote.css('p::text').extract()[0]
            # n2 = self.cleanData(body)
            # toPrint1 = test.convertBijoyToUnicode(n2)
            items['label'] = label
            items['title'] = title
            items['body'] = body
            yield items
        next_page = 'https://www.dailyinqilab.com/newscategory/sports/?page='+str(ProtidinSpider.page_number)+''
        print(next_page)
        if ProtidinSpider.page_number < 837:
            ProtidinSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)

