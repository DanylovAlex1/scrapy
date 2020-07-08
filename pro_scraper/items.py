# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Dog(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    location = scrapy.Field()
    #img_url = scrapy.Field()
