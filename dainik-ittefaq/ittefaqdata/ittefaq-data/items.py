# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProtidindataItem(scrapy.Item):
    body = scrapy.Field()
    label = scrapy.Field()
    title = scrapy.Field()
    source = scrapy.Field()

